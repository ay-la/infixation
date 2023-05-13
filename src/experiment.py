import openai
import random
import csv
import time

from modules.model_response import *
from modules.experiment_results import *
from tqdm import tqdm

openai.api_key = "YOUR_KEY_HERE"

def ask_model(prompt, model_name):
    response = openai.Completion.create(
        engine=model_name,
        prompt=prompt,
        temperature=0,
        max_tokens=50,
        n=1,
        stop=None,
        timeout=10,
        logprobs=3
    )
    return response

def generate_result(prompt, 
                    word, 
                    correct_infix, 
                    set_of_examples,
                    model_name):
    response = ask_model(prompt, model_name)
    response_text = response.choices[0].text.strip()
    logprobs = response["choices"][0]["logprobs"]["top_logprobs"]
    return ModelResponse(word, correct_infix, set_of_examples, response_text, logprobs)

def get_data(file_path):
    return load_csv_to_list(file_path)

def get_example_set(data, sampled_dict, test_word, num_shots):
    i = 0
    examples = []

    while i < num_shots:
        random_example = random.choice(data)

        if random_example[0] != test_word and random_example not in examples:
            if sampled_dict[random_example] == 0:
                examples.append(random_example)
                sampled_dict[random_example] += 1
                i += 1  
            else:
                sorted_dict = sorted(sampled_dict.items(), key=lambda item: item[1])

                j = 0
                while True:
                    alternative = sorted_dict[j][0]
                    if alternative[0] != test_word and alternative not in examples:
                        examples.append(alternative)
                        sampled_dict[alternative] += 1
                        i += 1
                        break
                    else:
                        j += 1

    return examples, sampled_dict

def run_gpt_expletive_experiment(num_shots, experiment_number, experiment_name, model_name, context, promptDetails, filePath):
   
    experiment = ExperimentResults(num_shots, experiment_number, experiment_name=experiment_name, model_name=model_name)
    data = get_data(filePath)
    sampled_dict = {item: 0 for item in data}

    for word_tup in enumerate(tqdm(data)):
        examples = [] # just to be sure that examples are getting reset..
        word = word_tup[1][0]
        correct_infix = word_tup[1][1]
        examples, sampled_dict = get_example_set(data, sampled_dict, word, num_shots)

        prompt = f"{context}{promptDetails[0]}{word}{promptDetails[1]}{str(len(examples))}{promptDetails[2]}{get_example_str(examples)}."
        print(prompt)

        try: 
            response = generate_result(prompt, word, correct_infix, examples, model_name)
        except openai.error.RateLimitError:
            print("\nRate limit reached. Trying again in 1 min.")
            countdown(61)
            response = generate_result(prompt, word, correct_infix, examples, model_name)

        # print()
        # print(response.examples)
        # print(response.word, response.result, response.predicted_correctly)
        # prompt_to_continue()
        experiment.add_result(response)

    experiment.save_to_file()

def get_example_str(examples):
    examples = ""
    for i, example in enumerate(examples):
        if (i < len(examples) - 1):
            examples += example[0] + ": " + example[1] + ", "
        else:
            examples += example[0] + ": " + example[1]
    return examples

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

def print_response(word, response):
    print(f"\nWORD: {word}")
    print("RESULTS:")
    for i, res in enumerate(response):
        print(f"{i+1} examples: {res}")
    print()

def load_csv_to_list(file_path):
    data = []
    with open(file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            word = row[0]
            infix = row[1]
            data.append((word, infix))
    return data

def prompt_to_continue():
    print()
    input("Enter to continue.")



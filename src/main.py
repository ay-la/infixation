from experiment import run_experiment, prompt_to_continue

if __name__ =="__main__":

    experiments = ['expletive', 'diddly', 'iz']

    contexts = [ "Expletive infixation is a process by which an expletive or profanity is inserted into a word, usually for intensification.", 
                 "Diddly infixation is a process by which the nonsense word 'diddly' is inserted into another word before a stressed syllable, " \
                 "and triggers reduplication following the infix. This word game was made famous by Ned Flanders on the television show The Simpsons.",
                 "-iz- infixation is a process by which -iz- or -izn- is inserted into a word, popularized by hip-hop artists like Snoop Dogg."  
                 ]

    prompts = [ ("\nInfix the expletive 'fuckin' into the word '", "' based on the following ", " example(s): "),
                ("\nInfix 'diddly' the word '", "' based on the following "," example(s): "),
                ("\nInfix -iz- or -izn- into the word '", "' based on the following ", " example(s): ")
              ]

    model_name = 'text-davinci-002'
    experiment_name = 'expletive'
    context = contexts[0]
    prompt = prompts[0]
    datapath = 'data/200_expletive_examples.csv'
    
    for num_shots in range(1,4):
        for experiment_number in range(1,4):
                print('===================================')
                print('# shots:', num_shots)
                print('Experiment #:', experiment_number)
                print('===================================')
                run_experiment(num_shots, experiment_number, experiment_name, model_name, context, prompt, datapath)


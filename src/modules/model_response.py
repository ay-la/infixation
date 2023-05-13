import string

class ModelResponse:
    def __init__(self, word, correct_infix, examples, result, logprobs):
        self.word = word
        self.correct_infix = correct_infix
        self.examples = examples
        self.num_examples = len(examples)
        self.result = result
        self.predicted_correctly = (correct_infix.lower() in self.clean_result(result)) or (correct_infix.replace('-', '').lower() in self.clean_result(result))
        self.logprobs = logprobs

    def clean_result(self, result):
        result_str = result.lower()
        punctuations = string.punctuation.replace("-", "")
        clean_result = ''.join(char for char in result_str if char not in punctuations)
        return clean_result.split()

    def __str__(self):
        return f"ModelResponse(word={self.word},\n num_examples={self.num_examples},\n examples={self.examples},\n result={self.result},\n predicted_correctly={self.predicted_correctly},\n logprobs={self.logprobs})"
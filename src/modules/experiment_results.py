import json
import os

class ExperimentResults:
    '''
    A class defining an object to store the results of one run of an experiment.

    Attributes
    ----------
    num shots : str
        The number of examples given to the model.
    experiment_number : int
        The trial number of the experiment; this assumes experiments are run for more than one trial.
    experiment_name : str
        The string representing the type of infixation.
    model_name : str
        The OpenAI model name.
    entries : dict
        The dictionary where results are stored. The test word is the key of the dictionary, and the values are a dictionary storing number of examples, list of examples, result generated by the model, the correct infix, whether or not the model's prediction was correct, and the set of top 3 logprobs for possible generated tokens.
    '''
    def __init__(self, num_shots: int, experiment_number: int, experiment_name: str, model_name: str):
        self.num_shots = num_shots
        self.experiment_number = experiment_number
        self.experiment_name = experiment_name
        self.model_name = model_name
        self.entries = {}

    def __str__(self):
        return f"ExperimentResults(experiment_name={self.experiment_name},\nnum_shots={self.num_shots},\nexperiment_number={self.experiment_number},\nentries={self.entries})"
    
    def add_result(self, model_response): 
        '''Stores a new model response in the experiment results.'''
        if (model_response.word in self.entries):
            raise ValueError('Word is already in the experiment results.')
        
        self.entries[model_response.word] = {"num_examples": model_response.num_examples,
                                                "examples" : model_response.examples,
                                                "result": model_response.result,
                                                "correct_infix": model_response.correct_infix,
                                                "predicted_correctly": model_response.predicted_correctly,
                                                "logprobs": model_response.logprobs}


    def save_to_file(self):
        '''Saves experiment results to a .json file.'''
        folder_name = self.model_name + "_results_v2"

        if not os.path.isdir(folder_name):
            os.mkdir(folder_name) 

        filename = self.experiment_name + "_" + str(self.num_shots) + "shot_exp" + str(self.experiment_number) + '_200'

        path = folder_name + "/" + filename + ".json"

        with open(path, "w") as write_file:
            json.dump(self.entries, write_file, indent=4)

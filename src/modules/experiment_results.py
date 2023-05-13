import json
import os

class ExperimentResults:
    '''
    A class defining an object to store the results of one run of an experiment.
    '''
    def __init__(self, num_shots, experiment_number, experiment_name, model_name):
        self.num_shots = num_shots
        self.experiment_number = experiment_number
        self.experiment_name = experiment_name
        self.model_name = model_name
        self.entries = {}

    def __str__(self):
        return f"ExperimentResults(experiment_name={self.experiment_name},\nnum_shots={self.num_shots},\nexperiment_number={self.experiment_number},\nentries={self.entries})"
    
    def add_result(self, model_response):  
        if (model_response.word not in self.entries):
            self.entries[model_response.word] = {"num_examples": model_response.num_examples,
                                                 "examples" : model_response.examples,
                                                 "result": model_response.result,
                                                 "correct_infix": model_response.correct_infix,
                                                 "predicted_correctly": model_response.predicted_correctly,
                                                 "logprobs": model_response.logprobs}
        else:
            pass # should be an exception that this word is already in the dict

    def save_to_file(self):
        folder_name = self.model_name + "_results_v2"

        if not os.path.isdir(folder_name):
            os.mkdir(folder_name) 

        filename = self.experiment_name + "_" + str(self.num_shots) + "shot_exp" + str(self.experiment_number) + '_200'

        path = folder_name + "/" + filename + ".json"

        with open(path, "w") as write_file:
            json.dump(self.entries, write_file, indent=4)

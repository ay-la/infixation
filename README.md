# LLM Infixation

This is the codebase for an exploratory evaluation of LLM behavior when tasked with English infixation using OpenAI's model API.

## Data

The dataset for these experiments can be found in `data/infix_dataset`, also [here](https://docs.google.com/spreadsheets/d/1-eyzKrxogjObyHk8BfMmvmC2zWkwzdXNWeTwhUZSDV4/edit?usp=sharing).
This data is a compilation of words and their syllable data in `data/syllable_data/`, `data/syllable_data/all_syllable_data.csv` generated from the [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) (`data/syllable_data/cmudict.rep`), plus their infixed forms which are generated by a set of heuristics particular to a type of infixation.

The experiments in this project do not directly interface with this dataset, which was generated by the code available in `data/generate_data.ipynb` preceding the section `Creating subsets of data`.
In its current state, the dataset is read into a dataframe and subsets of data are generated by randomly sampling $n$ rows of the dataframe. 
This provides an opportunity for a user to vet the examples given to the model.
Ideally the dataset will be reduced to exclude uncertain examples so that this step can be removed.
Currently, the only set of examples that has been vetted in this way is in the file `data/200_expletive_examples.csv`.
`data/old/` contains the original 100 hand-picked examples used prior to the construction of this dataset.

Dependecies for data generation:
- BeautifulSoup
- numpy
- pandas

## Running experiments

To prototype the experiment, OpenAI's API was used. 
To run the experiments, an API key must be entered on line 10 of `src/experiment.py`.
Experiments are run by running the `src/main.py` script.
In its current state, running the script by default runs the expletive experiment from 0 to 3 shots, with 3 runs of each number of shots, using the 200 expletive examples and the `text-davinci-003` model.

Dependencies for experiments:
- openai
- tqdm

## Error analysis
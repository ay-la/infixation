from experiment import run_gpt_expletive_experiment
# from experiment import prompt_to_continue

if __name__ =="__main__":

    experiments = ['fuckin', 'diddly', 'iz']

    contexts = [ "Expletive infixation is a process by which an expletive or profanity is inserted into a word, usually for intensification.", 
                 "Diddly infixation is a process by which the nonsense word 'diddly' is inserted into another word before a stressed syllable, " \
                 "and triggers reduplication following the infix. This word game was made famous by Ned Flanders on the television show The Simpsons.",
                 "-iz- infixation is a process by which -iz- or -izn- is inserted into a word, popularized by hip-hop artists like Snoop Dogg."  
                 ]
    #prompts = [ "*context*\nInfix -iz- or -izn- into the word '*word*' based on the following *len(examples)* example(s): *examples*",
    #            "*context*\nInfix 'diddly' the word '*word*' based on the following *len(examples)* example(s): *examples*",
    #            "*context*\nInfix the expletive 'fuckin' into the word '*word*' based on the following *len(examples)* example(s): *examples*"
                #]
    prompts = [ ("\nInfix the expletive 'fuckin' into the word '", "' based on the following ", " example(s): "),
                ("\nInfix 'diddly' the word '", "' based on the following "," example(s): "),
                ("\nInfix -iz- or -izn- into the word '", "' based on the following ", " example(s): ")
              ]
    
    #files = [ "data/old/fuckin.csv", "data/old/diddly.csv", "data/old/iz.csv"]

    #savePath = [ "blahFuckin", "blahdiidly"]

    model_name = 'text-davinci-002'
    experiment_name = 'expletive'
    context = contexts[0]
    prompt = prompts[0]
    file = 'data/200_expletive_examples.csv'
    
    for num_shots in range(1,4):
        for experiment_number in range(1,4):
                print('===================================')
                print('# shots:', num_shots)
                print('Experiment #:', experiment_number)
                print('===================================')
                run_gpt_expletive_experiment(num_shots, 
                                                experiment_number, experiment_name, model_name, 
                                                context, prompt, file)


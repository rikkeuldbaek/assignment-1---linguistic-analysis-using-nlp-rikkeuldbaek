### Assignment 1 - Extracting linguistic features using SpaCy
## Cultural Data Science - Language Analytics 
# Author: Rikke Uldbæk (202007501)
# Date: 11th of May 2023

# (please note that some of this code has been adapted from class sessions)

# Loading packages and the NLP model
import argparse
import os
import pandas as pd
import spacy
nlp = spacy.load("en_core_web_md")
import re as re
import warnings 
warnings.filterwarnings('ignore')



### Creating argument
def input_parse():
    #initialise the parser
    parser = argparse.ArgumentParser()
    #add arguments
    parser.add_argument("--folder_name", type=str, default= "USEcorpus") 
    # parse the arguments from the command line 
    args = parser.parse_args()
    
    #define a return value
    return args #returning argument




########## Define a linguistic feature extraction function ######## 
def nlp_function(folder_name):

    # Prepare path for folder containing all 14 subfolder
    path = os.path.join(os.getcwd(), "in", folder_name)

    # Loop over USEcorpus-folder and create path each individual subfolder
    for folder in os.listdir(path):
        folder_path = os.path.join(os.getcwd(), "in", folder_name, f'{folder}') 

        # Create a dataframe for each subfolder
        df = pd.DataFrame(columns=["file", "adj_freq", "noun_freq", "adv_freq", "verb_freq", "person_count", "loc_count", "org_count"])

        # Loop over each file in subfolder 
        for file in os.listdir(folder_path):
            file_path = os.path.join(os.getcwd(), "in", "USEcorpus", f'{folder}', f'{file}') 
        
            # Read file
            with open(file_path,'r', encoding= "latin-1") as f:
                    text= f.read()

            # Remove punctuation
            text = re.sub(r"<.*?>", '', text)

            # Make doc object
            doc_object = nlp(text)

            ##### Relative Frequency #####
            # Preparing variables 
            total_num_words = len(doc_object) # used for calculating the relative frequency
            adj_count = 0 
            noun_count = 0
            adv_count = 0
            verb_count = 0

            # Loop
            for token in doc_object:
                if token.pos_ == "ADJ":
                    adj_count += 1 # adding 1 each time the token is adjective
                elif token.pos_ == "NOUN":
                    noun_count += 1 # adding 1 each time the token is a noun
                elif token.pos_ == "ADV":
                    adv_count += 1 # adding 1 each time the token is a adverb
                elif token.pos_ == "VERB":
                    verb_count += 1 # adding 1 each time the token is a verb

            # Count relative frequencies for adjectives, nouns, adverbs, and verbs
            adj_freq = round(adj_count / total_num_words * 10000, 2)
            noun_freq = round(noun_count / total_num_words * 10000, 2)
            adv_freq = round(adv_count / total_num_words * 10000, 2)
            verb_freq = round(verb_count / total_num_words * 10000, 2)

            ##### Counting Frequencies for Entities #####
            # Preparing lists
            person = []
            loc = []
            org =  []
            
            # Loop
            for ent in doc_object.ents:
                if ent.label_ == "PERSON":
                    person.append(ent.text) 
                elif ent.label_ == "LOC":
                    loc.append(ent.text)
                elif ent.label_ == "ORG":
                    org.append(ent.text)

            # Count frequencies of unique locations, persons and organisations
            person_count = len(set(person))
            loc_count = len(set(loc))
            org_count = len(set(org))

            # Append all variables to previously made dataframe
            df = pd.concat([df, pd.DataFrame([{"file":file, "adj_freq":adj_freq, "noun_freq": noun_freq, "adv_freq":adv_freq, "verb_freq":verb_freq, "person_count":person_count, "loc_count":loc_count, "org_count":org_count}])], ignore_index=True)

        # Write files from subdirectory into a .csv for each subdirectory
        outpath = os.path.join(os.getcwd(), "out", folder + ".csv")
        df.to_csv(outpath)

        #print message
        print("Currently done with " + folder)

    #print message
    print("Done!!!")



#### define a main function
def main():
    # run the input parse
    args = input_parse()
    # pass name to the nlp_function()
    nlp_function(args.folder_name) 

main()
import nltk
from nltk.parse import stanford

jarpath="/home/dmanik/nltk_data/stanford/jars"
english_modelpath="/home/dmanik/nltk_data/stanford/englishPCFG.ser.gz"

import os

os.environ['STANFORD_PARSER'] = jarpath
os.environ['STANFORD_MODELS'] = jarpath

parser = stanford.StanfordParser(model_path=english_modelpath)

parsed=parser.raw_parse("The strongest rain ever recorded in India shut down the financial hub of Mumbai, snapped communication lines, closed airports and forced thousands of people to sleep in their offices or walk home during the night, officials said today.")

for node in parsed:
    print node

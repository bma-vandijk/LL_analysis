# imports
import os
import csv
import random as rd
import pandas as pd
from frog import Frog, FrogOptions


# set up frog
frog = Frog(FrogOptions(parser=False, morph=False,
                            chunking=False, mwu=True,
                            ner=False))

# assign home dir
wd = os.getcwd()

# make a list of files
stories = [f for f in os.listdir(f'{wd}/Lowlands_transcripts') if '.txt' in f]



from textblob import TextBlob
from textblob.exceptions import MissingCorpusError
import os

# Clearing the terminal (or cmd)
def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
clear()

# Colors
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
END = "\033[0m"

welcome = f"""
{BLUE}|||||             ~ Tone Analyzer ~             |||||
{BLUE} ||||           {YELLOW}Coded By : AmirTyper            {BLUE}||||
{BLUE}  |||         {YELLOW}My Instagram : @amir_typer        {BLUE}|||
{BLUE}   ||        {YELLOW}https://github.com/AmirTyper      {BLUE} ||
{BLUE}    |                     V1                    {BLUE}|{END}
"""
print(welcome)

while True:
    # get input text from user
    text = input(f"{GREEN}Enter some text: {END}")
    
    if text == "":
        print(f"{RED}/* Text can't be empty.{END}")
        continue
    
    try:
        # create TextBlob object and get sentiment polarity
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        
        # determine sentiment based on polarity score
        if polarity > 0:
            print(f"\nAnalysis Result: {GREEN}Positive{END}")
        elif polarity < 0:
            print(f"\nAnalysis Result: {RED}Negative{END}")
        else:
            print(f"\nAnalysis Result: {YELLOW}Neutral{END}")
        print()
        # get most positive and most negative sentence
        most_positive_sentence = sorted(blob.sentences, key=lambda x: x.sentiment.polarity, reverse=True)[0]
        most_negative_sentence = sorted(blob.sentences, key=lambda x: x.sentiment.polarity)[0]
        
        # print most positive and most negative sentence
        print(f"/+ {GREEN}Most positive sentence:{END} {most_positive_sentence}")
        print(f"/- {RED}Most negative sentence:{END} {most_negative_sentence}")
        print()
        break
    except MissingCorpusError as e:
        # handle the exception if required corpus data is missing
        print(f"{RED}/* Error: {END}", e)
        print(f"{YELLOW}/! Please download the required NLTK corpus data by running the command 'python -m textblob.download_corpora' or using the NLTK downloader: http://nltk.org/data.html{END}")

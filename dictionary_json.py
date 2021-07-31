import json
import difflib  #library to compare texts
from difflib import SequenceMatcher #Basically provides the similarity ratio between the junk text and the actual word
from difflib import get_close_matches
#help(json.load)
data=json.load(open('data.json','r')) #opening the file
def meaning(word):
    if word in data:
     return data[word]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8))>0:
     a=input(f"Did you mean {get_close_matches(word,data.keys(),cutoff=0.8)[0]} instead? Enter Y if yes or N if no\n")
     if a=="Y":
         return data[get_close_matches(word,data.keys(),cutoff=0.8)[0]]
     elif a=="N":
         return "We do not have this word"
     else:
         return "Invalid Input"

    else:
       return "This word is not present"

word=input("Enter word: ")
a=word.lower()  #To turn all letters to lower case. This removes case sensitivity

n=meaning(a)
if type(n)==list:
 for item in n:
    print(item)
else:
    print(n)



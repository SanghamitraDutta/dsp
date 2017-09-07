#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing *text to read*, and the *number of words to generate*. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

import sys
import random
from collections import defaultdict


def readfile(in_file):
    with open(in_file) as f:
        text = f.read()
    return text


def nxt_wrds_dict(text): # Makes dict with Keys: words from file & Values: list of words that follow the key word in the file
    word_list = text.split() 
    d = defaultdict(list)
    for i in range(0,len(word_list)-1): # for loop goes up to penultimate word in file as no words follow the last word
        d[word_list[i]].append(word_list[i+1]) # for every word key append the value list with the word that follows the key in the file    
    return d


def markov_generator(nxt_word_dict, n):
    StartWordsList = [word for word in nxt_word_dict.keys() if word[0].isupper()] #List all keys with Capital letter as they start a sentence
    First_word = random.choice(StartWordsList) # find a random starting word
    Output_List = [First_word]
    i=1
    while i< n:
        NextWord = random.choice(nxt_word_dict[Output_List[-1]]) #for each output word(key) find next word randomly(from value list)
        Output_List.append(NextWord)
        i+=1    
    MarkovOutput = " ".join(Output_List)
    return MarkovOutput

if __name__ == '__main__':

    input_file = sys.argv[1]        # 2nd argument entered on terminal
    word_count = int(sys.argv[2])   # 3rd argument entered on terminal

    input_text = readfile(input_file)
    nextword_dict = nxt_wrds_dict(input_text)
    markov_text = markov_generator(nextword_dict, word_count)
    print(markov_text)
    #print(nextword_dict) 

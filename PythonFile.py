import re
import string

def printsomething():
  print("Hello from python!")

def PrintMe(v):
    print("You sent me: " + v)
    return 100

def SquareValue(v):
    return v*v

def getWords(filename):
    list_of_words = []
    file = open(filename, 'CS210_Project_Three_Input_File')
    for line in file:
        line = line.strip().split()
        list_of_words += line

    return list_of_words

def getCount(word):
    return getWords('CS210_Project_Three_Input_File').count(word)
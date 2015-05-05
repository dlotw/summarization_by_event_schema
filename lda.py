__author__ = 'LBJ'
from prepare_lda import *
import os

def buildSet(fileName):
    with open(fileName, 'r') as f:
        lines = f.readlines()
    words = set()
    for line in lines:
        word = line.strip()
        words.add(word)
    return words

if __name__ == '__main__':
    # try to save all the file's path
    doc_dir = os.listdir("./docs")
    wordList = 'prep_list'
    stopping_words = buildSet(wordList)
    print stopping_words
    for dd in doc_dir:
        tmp_doc = []
        # construct path string
        doc_str = "docs/"+dd+"/"
        print doc_str
        lda = Feed_lda(doc_str, stopping_words)

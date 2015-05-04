__author__ = 'zephyros'
import os
import nltk.tokenize
def Test2(rootDir):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        print(path)
        # if os.path.isdir(path):
        #     Test2(path)

Test2('./d04aNER/')

sen = 'hello this is jack'
words = nltk.tokenize.word_tokenize(sen)
print(words)
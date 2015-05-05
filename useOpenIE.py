__author__ = 'zephyrYin'
import os
from ScoreWords import ScoreWords
from Article import Article
from NameEntity import NE
import nltk.tokenize
import math

def loopDir(rootDir):
    d = []
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        d.append(path)
    return d

def setScore(words, scores):
    score = 0
    for word in words:
        if word in scores:
            score += scores[word]
    return score

sentenceScores = {}

fileNames = ['d04aOpenieResult/' + str(i+1) + '.txt' for i in range(7)]
articles = [Article(f) for f in fileNames]
articleWords = [article.wordFrequency for article in articles]

ne = NE(loopDir('./d04aNER'))
t = ScoreWords(articleWords, ne.dict)
scores = t.getScore()

tmp = sorted(scores.items(), key=lambda d :d[1], reverse=True)
# for s in tmp:
#     print(s)



for article in articles:
    for i in range(len(article.content)):
        line = article.content[i]
        words = article.extractionWords[i]
        score = setScore(words, scores)
        sentenceScores[line] = score


print_entity = sorted(sentenceScores.items(), key=lambda d :d[1]/math.log(len(nltk.tokenize.word_tokenize(d[0])),2), reverse=True)
#print_entity = sorted(sentenceScores.items(), key=lambda d :d[1], reverse=True)

for p in print_entity:
    print(p)
summary = ''
cnt = 0
lineCnt = 0
while cnt < 200:
    line = print_entity[lineCnt][0]
    summary += line + ' '
    lineCnt += 1
    cnt += len(nltk.tokenize.word_tokenize(line))
file = open('summary.txt','w')
file.write(summary)
file.close()




__author__ = 'zephyrYin'
import sys
from TfIdf import TfIdf
from Article import Article

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
t = TfIdf(articleWords)
scores = t.getScore()



for article in articles:
    for i in range(len(article.content)):
        line = article.content[i]
        words = article.extractionWords[i]
        score = setScore(words, scores)
        sentenceScores[line] = score


print_entity = sorted(sentenceScores.items(), key=lambda d :d[1], reverse=True)
summary = ''
for i in range(10):
    line = print_entity[i][0]
    summary += line + ' '
file= open('summary.txt','w')
file.write(summary)
file.close()




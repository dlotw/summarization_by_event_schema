__author__ = 'LBJ'
from nltk.tokenize import word_tokenize
import os
import math
import DIR

class Match_lda(object):
    def __init__(self, path):
        self.path = path

    def load_file(self):
        keywords = {}
        fileName = 'model-final.twords'
        file = self.path + fileName
        with open(file, 'r') as f:
            lines = f.readlines()
        for line in lines:
            ele = word_tokenize(line.strip())
            # print ele
            if 'Topic' in ele:
                continue
            else:
                keywords[ele[0]] = float(ele[1])
        return keywords

class Read_doc(object):
    def __init__(self, path, keywords):
        self.path = path
        self.sents = []
        self.keywords = keywords

    def load_file(self):
        docs = os.listdir(self.path)
        for doc in docs:
            file = self.path + doc
            with open(file, 'r') as f:
                lines = f.readlines()
            sent = []
            for line in lines:
                ele = word_tokenize(line.strip())
                for item in ele:
                    if item is not '.':
                        sent.append(item)
                    else:
                        sent.append(item)
                        self.sents.append(sent)
                        sent = []


    def summary(self, limit):
        indexAndScore = self.getSentenceRank()
        # print indexAndScore
        s = ''
        cnt = 0
        lineCnt = 0
        while cnt < limit:
            sent = self.sents[indexAndScore[lineCnt][0]]
            # print sent
            s += ' '.join(sent)
            lineCnt += 1
            cnt += len(sent)
        return s

    def getSentenceRank(self):
        self.load_file()
        # print self.sents
        score = [0 for i in range(len(self.sents))]
        # print score

        for i in range(len(self.sents)):
            sent = self.sents[i]
            for item in sent:
                if item in self.keywords:
                    score[i] -= math.log(self.keywords[item], 2)
        dict = {}
        for i in range(len(self.sents)):
            dict[i] = score[i]
        sentenceRank = sorted(dict.items(), key=lambda d: d[1], reverse=True)
        return sentenceRank


if __name__ == '__main__':
    doc_dir = os.listdir("./LDA_input")
    # print doc_dir
    i = 1
    for dir in doc_dir:
        print dir
        path = './LDA_input/'+dir+'/'
        doc_path = './openieInput/'+dir+'/'
        # print path
        lda_dict = Match_lda(path).load_file()
        # print lda_dict
        DIR.mkdir('./LDA_result')
        file = './LDA_result/'+'test'+str(i)+'_system'+'.txt'
        i += 1
        with open(file, 'w+') as f:
            f.write(Read_doc(doc_path, lda_dict).summary(200))



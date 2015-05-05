__author__ = 'LBJ'
import itertools
from nltk.tokenize import word_tokenize
import os

class Feed_lda():
    def __init__(self, doc_dir):
        self.dir = doc_dir
        self.docs = []
        self.read_file()
        self.write_file()

    def load_file(self, file):
        with open(file, 'r') as f:
            lines = f.readlines()
        flag = False
        sentence = []
        for line in lines:
            ele = word_tokenize(line.strip())
            # print ele
            if '/TEXT' in ele:
                flag = False
                continue
            elif flag is True:
                sentence.append(ele)
            elif 'TEXT' in ele:
                flag = True
                continue
        # print sentence
        self.docs.append(list(itertools.chain.from_iterable(sentence)))
        # print self.docs

    def read_file(self):
        docs_path = []
        tmp_doc = []
        dir = self.dir
        for k in os.listdir(dir):
            tmp_doc.append(dir+k)
        docs_path.append(tmp_doc)
        # print docs_path
        # Should be changed when test on other data set.
        for i in range(len(docs_path)):
            files = docs_path[i]
            # print files
            for file in files:
                self.load_file(file)
        # print self.docs

    def write_file(self):
        fileName = self.dir.strip('/').replace('docs/', '') + '.dat'
        print fileName
        dest_dir = './LDA_input/'
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        path = os.path.join(dest_dir, fileName)
        with open(path, 'w+') as f:
            f.write(str(len(self.docs))+'\n')
            for doc in self.docs:
                f.write(' '.join(doc)+'\n')
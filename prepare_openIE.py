__author__ = 'LBJ'

from nltk.tokenize import word_tokenize
import os

class Feed_openIE():
    def __init__(self, doc_dir):
        self.dir = doc_dir
        self.docs = {}
        self.write_file()

    def load_file(self, file):
        with open(file, 'r') as f:
            lines = f.readlines()
        flag = False
        sentence = []
        for line in lines:
            ele = line.strip().split()
            # print ele
            if '</TEXT>' in ele:
                flag = False
                continue
            elif '<P>' in ele:
                continue
            elif '</P>' in ele:
                continue
            elif flag is True:
                sentence.append(ele)
            elif '<TEXT>' in ele:
                flag = True
                continue

        return sentence

    def read_file(self):
        docs_path = []
        tmp_doc = []
        dir = self.dir
        content={}
        for k in os.listdir(dir):
            tmp_doc.append(dir+k)
        docs_path.append(tmp_doc)
        # print docs_path
        # Should be changed when test on other data set.
        for i in range(len(docs_path)):
            files = docs_path[i]
            # print files
            for file in files:
                print file
                content[file]=self.load_file(file)
        return content
        # print self.docs

    def write_file(self):
        content = self.read_file()
        for k in os.listdir(self.dir):
            fileName = k
            print fileName
            dest_dir = './OPENIE_input/'+self.dir.strip('/').replace('docs/', '')
            # print dest_dir
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            path = os.path.join(dest_dir, fileName)
            with open(path, 'w+') as f:
                # f.write(str(len(self.docs))+'\n')
                fileName = self.dir+fileName
                for doc in content[fileName]:
                    print doc
                    f.write(' '.join(doc)+'\n')
                # f.write(doc)

if __name__ == '__main__':
    # try to save all the file's path
    doc_dir = os.listdir("./docs")
    for dd in doc_dir:
        # construct path string
        doc_str = "docs/"+dd+"/"
        print doc_str
        openIE = Feed_openIE(doc_str)
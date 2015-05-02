# This class represent a document
# use a path to initiate Document
import re
from nltk.tokenize import sent_tokenize
import untangle

class Document:

    def __init__(self, path):
        # read in the data
        self.content = ""
        #self.title = ""
        #self.subtitle = ""
        self.load_file(path)
        self.sents = []



    def load_file(self, path):
        '''
        read all the information from file
        :param path: path of the path
        :return:
        '''
        obj = untangle.parse(path)
        content = obj.DOC.TEXT
        #content = obj.root.child['name']
        print(content)
        # f = open(file)
        # content = f.readlines()
        # f.close()
        # lines = []
        # for line in content:
        #     line = line.strip('\n')
        #     if(len(line) == 0):
        #         continue
        #     lines.append(line)
        # text = self.readXML(lines)
        #
        # # Don't use the title for now
        # # head_b = re.compile(r"<HEAD>")
        # # head_e = re.compile(r"</HEAD>")
        # # to identify text
        # text_b = re.compile(r"<TEXT>")
        # text_e = re.compile(r"</TEXT>")
        #
        # i = 0
        # while i in range(0, len(content)):
        #     # find content
        #     t_b = text_b.match(content[i])
        #     if t_b:
        #         tmp = []
        #         # matches <TEXT>
        #         j = i
        #         # we need to find <\TEXT>
        #         t_e = False
        #         while not t_e:
        #             tmp.append(content[j].replace("\n", " "))
        #             # if we can match we should stop looping
        #             t_e = text_e.search(content[j])
        #             j += 1
        #
        #         self.content = "".join(tmp)
        #
        #     i += 1
        # self.content = self.content.replace("<TEXT>", "").replace("</TEXT>", "")
        # self.sents = sent_tokenize(self.content)


if __name__ == "__main__":

    file = "d06a//AP890117-0132"
    #file = "d06aa//test.xml"
    #obj = untangle.parse(file)
    #content = obj.root.child['name']
    d06 = Document(file)



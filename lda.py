__author__ = 'LBJ'
from prepare_lda import *
import os

if __name__ == '__main__':
    # try to save all the file's path
    doc_dir = os.listdir("./docs")
    summary_dir = os.listdir("./summary")
    for dd in doc_dir:
        tmp_doc = []
        # construct path string
        doc_str = "docs/"+dd+"/"
        print doc_str
        lda = Feed_lda(doc_str)

__author__ = 'zephyros'

class Useless:
    def __init__(self, path):
        self.path = path
        self.words = []
        self.loadFile(self.path)

    def loadFile(self, path):
        file = open(path)
        lines = file.readlines()
        file.close()
        self.words = []
        for line in lines:
            self.words.append(line.strip('\n'))
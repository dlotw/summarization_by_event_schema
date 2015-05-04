__author__ = 'zephyros'

class NE:
    def __init__(self, path):
        self.path = path
        self.dict = self.loadFile(path)

    def loadFile(self, paths):
        documents = []
        for path in paths:
            file = open(path)
            documents.append(file.readlines())
            file.close()
        dict = {}
        for lines in documents:
            for line in lines:
                content = line[2:-3]
                tmp = content.split('), (')
                for t in tmp:
                    tuple = t.strip('(').strip(')')
                    temp = tuple.split(', ')
                    word = temp[0].strip('\'').lower()
                    entity = temp[1].strip('\'')
                    if not entity in dict:
                        dict[entity] = [word]
                    else:
                        if not word in dict[entity]:
                            dict[entity].append(word)
        for d in dict:
            print(d)
        return dict

if __name__ == "__main__":
    ne = NE(['d04aNER/FT923-5089','d04aNER/FT923-5267','d04aNER/FT923-5797','d04aNER/FT923-5835','d04aNER/FT923-6038','d04aNER/FT923-6110','d04aNER/FT923-6455'])
    print(ne.dict['PERSON'])

# Class to represent schema
import nltk.tokenize as tokenizer
from nltk.corpus import wordnet as wn
class Schema:

    def __init__(self, id = -1, fileName = ""):
        self.schema_id = id
        # a list of Rule object(see below)
        # represent all the rules in event_schema
        self.rule_list = []
        self.fileName = fileName
        self.loadSchema()

    def loadSchema(self):
        file = open(self.fileName)
        lines = file.readlines()
        file.close()

        for line in lines:
            tuples = line.rstrip('\n').split('\t')
            if int(tuples[1]) == self.schema_id:
                rule = Rule(tuples[2:7])
                self.rule_list.append(rule)
            else:
                if len(self.rule_list) > 0:
                    break

    def matchSentence(self, sentence):
        '''
        A sentence to match to this schema
        :param sentence: Sentence to be matched (a string)
        :return: matched or not
        '''

    def matchSentenceWithRule(self, rule_id, sentence):
        '''
        This function should be called by matchSentence
        :param rule_id: which rule use to match the sentence
        :param sentence: sentence to be matched
        :return: matched or not
        '''

        # for a given sentence, we test if we can match this sentence
        # with the rule_id specified
        rule = self.rule_list[rule_id]
        rule.display()
        words = tokenizer.word_tokenize(sentence)
        print(words)






# Rule represent one line of the event schema
# One rule in event schema
class Rule:

    def __init__(self, r):
        # instance for arg1
        self.arg1_ins = []
        self.arg1 = ""
        self.rel = ""
        self.arg2 = ""
        self.arg2_ins = []
        self.loadRule(r)

    def loadRule(self, tuple_five):
        '''
        Given one string, which is one line in schema.txt
        generate Rule by using this funcion
        :param tuple_five: a five element list (generated by Schema's load_schema function)
        :return: None, just used for initiate the class
        '''
        self.arg1_ins = tuple_five[0]
        self.arg1 = tuple_five[1]
        self.rel = tuple_five[2]
        self.arg2 = tuple_five[3]
        self.arg2_ins = tuple_five[4]

    def display(self):
        print(str(self.arg1_ins) + ' ' + self.arg1 + ' ' + self.rel + ' ' + self.arg2 + ' ' + str(self.arg2_ins))






if __name__ == "__main__":
    schema = Schema(1, "chosen_schema")

    sent = "Gates did not resign until the following year after the acquittal of the four officers caused massive rioting."
    schema.matchSentenceWithRule(0, sent)





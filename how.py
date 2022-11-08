import stanza
from nltk.tree import Tree as Tree
import binaries
class How:
    def __init__(self,pipeline) -> None:
            self.nlp=pipeline
            pass
    def is_how_many(self,text,tree):
        '''
            Find numbers in string and figure out whether 
            the sentence is binary-able or not
        '''
        for i in self.nlp(text[0]).sentences[0].words:
            if i.deprel =='nummod':
                return binaries.Binary(self.nlp).isBinary(tree)
        return False
    def main(self,text):
        '''
            Find the number phrase and alter the string
            to a question form
        '''
        doc=self.nlp(text[0])
        tree = doc.sentences[0].constituency
        tree = Tree.fromstring(str(tree))
        if not self.is_how_many(text,tree):
            return None 
        subject=self.find_subject(doc)
        sub=subject[1]
        subject=' '.join(subject)+' '
        result=binaries.Binary(self.nlp).main(text[0]).replace(subject,'')
        return ['how many ' +sub+' '+result,text[1],subject[0]]
    def find_subject(self,doc):
        for i in range(len(doc.sentences[0].words)):
            if doc.sentences[0].words[i].deprel =='nummod':
                return [doc.sentences[0].words[i].text,doc.sentences[0].words[i+1].text]



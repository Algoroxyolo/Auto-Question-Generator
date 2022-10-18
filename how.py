import stanza
from nltk.tree import Tree as Tree
import binaries
class How:
    def __init__(self) -> None:
            self.nlp=stanza.Pipeline(processors='tokenize,pos,lemma,pos,constituency,depparse,ner', tokenize_pretokenized=True)
            pass
    def is_how_many(self,text,tree):
        '''
            Find numbers in string and figure out whether 
            the sentence is binary-able or not
        '''
        for i in self.nlp(text).sentences[0].words:
            print(i.deprel,i.text)
            if i.deprel =='nummod':
                return binaries.Binary().isBinary(tree)
        return False
    def main(self,text):
        '''
            Find the number phrase and alter the string
            to a question form
        '''
        doc=self.nlp(text)
        tree = doc.sentences[0].constituency
        tree = Tree.fromstring(str(tree))
        if not self.is_how_many(text,tree):
            print ("It could not be converted to why question.")
            return None 
        subject=self.find_subject(doc)
        sub=subject[1]
        subject=' '.join(subject)+' '
        result=binaries.Binary().main(text).replace(subject,'')
        return 'how many ' +sub+' '+result
    def find_subject(self,doc):
        for i in range(len(doc.sentences[0].words)):
            if doc.sentences[0].words[i].deprel =='nummod':
                return [doc.sentences[0].words[i].text,doc.sentences[0].words[i+1].text]


print(How().main(''))
'how many weeks will the term project take place over at the end of the semester'
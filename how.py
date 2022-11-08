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
        subject=self.find_subject(tree)
        sub=' '.join(subject[1:])
        subject=' '.join(subject)
        result=binaries.Binary(self.nlp).main(text[0])
        result=result.replace(subject,'')
        return ['how many ' +sub+' '+result,text[1],subject]
    def find_subject(self,tree):
        for t in tree[0]:
            if t.label()=='VP':
                for subtree in t:
                    if subtree.label()=='NP':
                        return subtree.leaves()


        
print(How(stanza.Pipeline(processors='tokenize,pos,lemma,pos,constituency,depparse,ner', tokenize_pretokenized=True)).main(['Thomas has 16 sweet apples',1]))

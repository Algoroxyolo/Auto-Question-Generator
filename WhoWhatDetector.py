from nltk.tree import Tree as Tree
from binaries import *
import stanza

class WhatWho:
    def __init__(self) -> None:
        self.nlp=stanza.Pipeline(processors='tokenize,pos,lemma,pos,constituency,depparse,ner', tokenize_pretokenized=True)
        pass
    def is_who(self,text):
        '''
           determine if the noun of the sentence is a person or 
           not a person. If it is a person, return true and the noun.

        '''
        doc=self.nlp(text)
        tree=Tree.fromstring(str(doc.sentences[0].constituency))
        for t in tree[0]:
            if t.label() == "NP":
                res=[]
                for subtree in t:
                    res.append(" ".join(subtree.leaves()))    
        res=' '.join(res)
        who_tester=self.nlp(res).sentences[0].ents
        if who_tester==[]:
            return False,res
        return True,res

    def __main__(self,text):
        (isWho,res)=self.is_who(text)
        if isWho:
            text=text.replace(res,'Who')
        else:
            text=text.replace(res,'What')
        text=text.replace('.','?')
        text=text.replace('!','?')
        return text
        
        
print(WhatWho().__main__("Sunaya is a CMU student ?"))
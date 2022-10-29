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
        print(text[0])
        doc=self.nlp(text[0])
        tree=Tree.fromstring(str(doc.sentences[0].constituency))
        print(tree)
        for t in tree[0]:
            print(t)
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
            text[0]=text[0].replace(res,'Who')
            text.append(res)
        else:
            text[0]=text[0].replace(res,'What')
            text.append(res)
        text[0]=text[0].replace('.','?')
        text[0]=text[0].replace('!','?')
        return text
        
        
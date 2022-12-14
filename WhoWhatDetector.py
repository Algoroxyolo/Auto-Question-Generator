from nltk.tree import Tree as Tree
from binaries import *
import stanza
from where import Where
class WhatWho:
    def __init__(self,pipeline) -> None:
        self.nlp=pipeline
        pass
    def is_who(self,text):
        '''
           determine if the noun of the sentence is a person or 
           not a person. If it is a person, return true and the noun.
           else decides whether it is a location or something else.
           We also look at whether noun phrase is a pronoun or not.

        '''
        doc=self.nlp(text[0])
        tree=Tree.fromstring(str(doc.sentences[0].constituency))
        for t in tree[0]:
            if t.label() == "NP":
                res=[]
                for subtree in t:
                    if subtree.label()=="PRP":
                        prp=subtree.leaves()
                    res.append(" ".join(subtree.leaves()))    
        res=' '.join(res)
        who_tester=self.nlp(res).sentences[0].ents
        for i in who_tester:
            if i.type=='PERSON':
                return 'who',res
            elif i.type=='LOC':
                return 'where',res
            else:
                return 'what',res
        if prp[0].lower() in ['he','she','they','i','you']:
            return 'who',res
    def __main__(self,text):
        (isWho,res)=self.is_who(text)
        if isWho=='who':
            text[0]=text[0].replace(res,'Who')
            text[0]=text[0].replace('am','is')
            text.append(res)
        elif isWho=='what':
            text[0]=text[0].replace(res,'What')
            text.append(res)
        elif isWho=='where':
            text[0]=text[0].replace(res,'where')
            text.append(res)
        return text

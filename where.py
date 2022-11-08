from nltk.tree import Tree as Tree
from binaries import Binary
import stanza
class Where:
    def __init__(self,pipeline):
        self.nlp=pipeline
        pass
    def is_where(self,doc):
        '''
            Scan through the sentence, if the sentence have 
            location or a GPE go on and check if it has a positional
            indicator.
        '''
        a=0
        location=''
        for i in doc.sentences[0].ents:
            if i.type=="LOC" or i.type=='GPE':
                a=1
                ref=i.text
        tree = doc.sentences[0].constituency
        tree = Tree.fromstring(str(tree))
        if a==1:
            for t in tree[0]:
                if t.label()=='PP':
                    location=" ".join(t.leaves())
                    a+=1
                    break
                if t.label()=='VP':
                    for subtree in t:
                        if subtree.label()=='PP':
                            location=" ".join(subtree.leaves())
                            #make sure that the pp is followed by time
                            if ref in location:
                                a+=1
                                break
                        if subtree.label()=='VP':
                           for subsubtree in subtree:
                                if subsubtree.label()=='PP':
                                    location=" ".join(subsubtree.leaves())
                                if ref in location:
                                    a+=1
                                    break
        if a==2:
            return True,location
        return False,None
    def main(self, text):
        '''
            Find the time component in the sentence.
            assemble the sentence into a where question

        '''
        doc = self.nlp(text[0])
        when,location=self.is_where(doc)
        if not when:
            return False
        res= Binary(self.nlp).main(doc.sentences[0].text)
        res=res.replace(location,'')
        return ["Where "+res,text[1],location]
    

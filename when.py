from nltk.tree import Tree as Tree
from binaries import Binary
import stanza
class When:
    def __init__(self,pipeline):
        self.nlp=pipeline
        pass
    def is_when(self,doc):
        '''
            Scan through the sentence, if the sentence have 
            Time or date go on and check if it has a positional
            indicator. If also that, check for the sentence is
            binary-able or not.
        '''
        a=0
        time=''
        for i in doc.sentences[0].ents:
            if i.type=="DATE" or i.type=='TIME':
                a=1
                ref=i.text
        tree = doc.sentences[0].constituency
        tree = Tree.fromstring(str(tree))
        if a==1:
            print(tree)
            for t in tree[0]:
                if t.label()=='PP':
                    time=" ".join(t.leaves())
                    a+=1
                    break
                if t.label()=='VP':
                    for subtree in t:
                        if subtree.label()=='PP':
                            time=" ".join(subtree.leaves())
                            #make sure that the pp is followed by time
                            if ref in time:
                                a+=1
                                break
                        if subtree.label()=='VP':
                           for subsubtree in subtree:
                                if subsubtree.label()=='PP':
                                    time=" ".join(subsubtree.leaves())
                                if ref in time:
                                    a+=1
                                    break
        if a==2:
            return True,time
        return False,None
    def main(self, text):
        '''
            Find the time component in the sentence.
            assemble the sentence into a when question

        '''
        doc = self.nlp(text[0])
        when,time=self.is_when(doc)
        if not when:
            return False
        res= Binary(self.nlp).main(doc.sentences[0].text)
        res=res.replace(time,'')
        return ["When "+res,text[1],time]
    

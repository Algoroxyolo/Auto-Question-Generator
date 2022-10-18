from nltk.tree import Tree as Tree
from binaries import Binary
import stanza
class When:
    def __init__(self) -> None:
        self.nlp=stanza.Pipeline(processors='tokenize,pos,constituency,lemma,ner', tokenize_pretokenized=True)
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
            print(i.type)
            if i.type=="DATE" or i.type=='TIME':
                a=1
                print('checkPoint 1')
        tree = doc.sentences[0].constituency
        tree = Tree.fromstring(str(tree))
        if a==1:
            for t in tree[0]:
                print(t.label())
                if t.label() == "VP":
                    for subtree in t:
                        if subtree.label()=='PP':
                            time=' '.join(subtree.leaves())
                            a+=1
                            print('check point 2')
                if t.label()=='PP':
                    time=' '.join(t.leaves())
                    a+=1
                    print('check point 2')
        if a==2:
            return Binary().isBinary(tree),time
        return False,'FUCK YOU'
    def main(self, text):
        doc = self.nlp(text)
        when,time=self.is_when(doc)
        if not when:
            print ("It could not be converted to when question.")
            return None
        res= Binary().main(doc.sentences[0].text)
        res=res.replace(time,'')
        return "When "+res
       


print(When().main('15-122 is at 8 am'))
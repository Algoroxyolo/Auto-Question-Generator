import stanza
from sentenceSeperator import tokenizer
from nltk.tree import Tree as Tree
class parser():
    def __init__(self,dir,lstData):
        self.data=tokenizer(dir,lstData,top_K=True,k=10)
        pass

    def parse(self):
        nlp=stanza.Pipeline(processors='tokenize,pos,constituency', tokenize_pretokenized=True)
        doc=nlp(self.data)
        lst=[]
        upos=[]
        for i in range(len(doc.sentences)):
            print(doc.sentences[i].text)
            for j in range(len(doc.sentences[i].words)):
                upos.append(doc.sentences[i].words[j].xpos)
            lst.append(upos)
            #print(upos)
            upos=[]
        return lst


#data=tokenizer('data/noun_counting_data',['a1.txt'])
text=parser('data/noun_counting_data',['new.txt'])
print(parser.parse(text))
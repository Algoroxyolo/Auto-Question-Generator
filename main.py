from sentenceSeperator import tokenizer
from when import When
from Why import Why
from binaries import Binary
from how import How
import evaluation
from WhoWhatDetector import WhatWho
import stanza
class main:
    def __init__(self):
        self.pipeline=stanza.Pipeline(processors='tokenize,pos,lemma,pos,constituency,depparse,ner', tokenize_pretokenized=True)
        self.WhatWHo=WhatWho(self.pipeline)
        self.binary=Binary()
        pass
    def __main__(self,text,filename):
        lst=tokenizer(text,filename)
        questionList=[]
        for i in lst:
            print(i)
            d=i.copy()
            if self.binary.main(d[0]):
                lst1=[]
                lst1.append(self.WhatWHo.__main__(d))
                d=i
                lst1.append(When(self.pipeline).main(d))
                d=i
                lst1.append(How(self.pipeline).main(d))
                d=i
                lst1.append(Why(self.pipeline).main(d))
                d=i
                for j in lst1:
                    print(j)
                    if j!=None:
                        questionList.append(j)
        return self.output(questionList,filename)
    
    def output(self,questionlist,filename):
        file=open(f'{filename} -q.txt','w+')
        for i in questionlist:
            file.write(f'{i[0]}\t{i[1]}\t{i[2]}\n')
        file.close()


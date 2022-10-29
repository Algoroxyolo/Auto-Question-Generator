from sentenceSeperator import tokenizer
from when import When
from Why import Why
from binaries import Binary
from how import How
import evaluation
from WhoWhatDetector import WhatWho
class main:
    def __init__(self):
        pass
    def __main__(self,text):
        lst=tokenizer(text)
        questionList=[]
        for i in lst:
            print(i)
            d=i.copy()
            if Binary().main(d[0]):
                lst1=[]
                lst1.append(WhatWho().__main__(d))
                d=i
                lst1.append(When().main(d))
                d=i
                lst1.append(How().main(d))
                d=i
                lst1.append(Why().main(d))
                d=i
                for j in lst1:
                    print(j)
                    if j!=None:
                        questionList.append(j)
        return self.output(questionList)
    def output(self,questionlist):
        file=open('question.txt','w+')
        for i in questionlist:
            file.write(f'{i[0]}\t{i[1]}\t{i[2]}\n')
        file.close()


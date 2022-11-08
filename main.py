from sentenceSeperator import tokenizer
from when import When
from Why import Why
from binaries import Binary
from how import How
from beautification import beautify
from WhoWhatDetector import WhatWho
from where import Where
import stanza
import random
class main:
    def __init__(self):
        self.pipeline=stanza.Pipeline(processors='tokenize,pos,lemma,pos,constituency,depparse,ner', tokenize_pretokenized=True)
        self.WhatWHo=WhatWho(self.pipeline)
        self.binary=Binary(self.pipeline)
        pass
    def __main__(self,text,filename):
        '''
            For each sentence inputed try to get each sentence type.
            Put valid questions into the question list.
        '''
        lst=tokenizer(text,filename)
        questionList=[]
        for i in lst:
            d=i.copy()
            if self.binary.main(d[0]):
                questionLst=[]
                questionLst.append(self.WhatWHo.__main__(d))
                d=i
                questionLst.append(When(self.pipeline).main(d))
                d=i
                questionLst.append(How(self.pipeline).main(d))
                d=i
                questionLst.append(Why(self.pipeline).main(d))
                d=i
                questionLst.append(Where(self.pipeline).main(d))
                d=i
                for j in questionLst:
                    if j!=None and j!=False:
                        questionList.append([beautify(j[0])]+j[1:])
        random.shuffle(questionList)
        return self.output(questionList,filename)
    
    def output(self,questionlist,filename):
        '''
            output the questions in a seperated file
            tag the question as -q
        '''
        file=open(f'QuestionFile\{filename} -q.txt','w+')
        for i in questionlist:
            file.write(f'{i[0]}\t{i[1]}\t{i[2]}\n')
        file.close()


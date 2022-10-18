from nltk.tokenize import sent_tokenize,word_tokenize
from datasets import load_dataset
import string
def tokenizer(path,dataset,top_K=False,k=None):
    '''
        tokenize the dataset and filter the good
        sentences. If top_k is true, find the 
        top k sentences
    '''
    sentencelst=[]
    data=load_dataset(path,data_files={"validation": dataset})
    for datum in data["validation"]:
        sentencelst.append(sent_tokenize(datum['text']))
    lst1=[]
    for para in sentencelst:
        if para!=[]:
            for sentence in para:
                sentence.replace('{','')
                sentence.replace('}','')
                sentence.replace('\n','')
                lst1.append(sentence)
    lst2=[]
    set1=[]
    for sentence in lst1:
        if (len(word_tokenize(sentence))>6 and '?' not in sentence and '(' not in sentence):
            lst2.append(word_tokenize(sentence))
            set1.append(sentence)
            set1=list(set(set1))

    if top_K==True:
        result=[]
        sentences_top_k = sorted(set1, key = len)[:k]
        for i in range(len(sentences_top_k)):
            result.append(word_tokenize(sentences_top_k[i]))
        return result
    return lst2

def num_Punct(str1):
    punc=string.punctuation
    num=0
    for i in str1:
        if i in punc:
            num+=1
    return num


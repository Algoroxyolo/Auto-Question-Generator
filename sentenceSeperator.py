from nltk.tokenize import sent_tokenize,word_tokenize
import nltk
from datasets import load_dataset
import string
def tokenizer(text,top_k=False,k=None):
    '''
        tokenize the dataset and filter the good
        sentences. If top_k is true, find the 
        top k sentences
    '''
    sentencelst=[]
    sentencelst.append(sent_tokenize(text))
    lst1=[]
    for para in sentencelst:
        if para!=[]:
            for sentence in para:
                sentence.replace('{','')
                sentence.replace('}','')
                sentence.replace('\n','')
                sentence.replace(',',' , ')
                sentence.replace('.',' . ')
                lst1.append(sentence)
    lst2=[]
    set1=[]
    for i in range(len(lst1)):
        if (len(word_tokenize(lst1[i]))>3 and '?' not in lst1[i] and '(' not in lst1[i]):
            lst2.append([lst1[i],i+1])
            set1.append(lst1[i])
            set1=list(set(set1))

    if top_k==True:
        result=[]
        sentences_top_k = sorted(set1, key = len)[:k]
        for i in range(len(sentences_top_k)):
            result.append(sentences_top_k[i])
        return result
    
    file=open('text.txt','w+')
    for i in lst2:
        file.write(f'{i[0]}\t{i[1]}\n')
    file.close()
    return lst2

def num_Punct(str1):
    punc=string.punctuation
    num=0
    for i in str1:
        if i in punc:
            num+=1
    return num



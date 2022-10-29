import nltk
import collections
import matplotlib.pyplot as plt
def TextOverview(content):
    textList=[]
    total_list=[]
    punctuations=[',','.','(',')','"','!',"'","[","]","&"]
    for punct in punctuations:
        content=content.replace(punct,' ')
    for words in content.split(' '): 
        word_token = nltk.word_tokenize(text=words)
        #disgard reoccuring words
        textList=textList+word_token
        textList=list(set(textList))
        #calculate total word count
        total_list=total_list+word_token
    #find the occurence of each word and find the most frequent occuring one
    frequency_count=collections.Counter(total_list)
    #find the frequency of words of each one
    frequency_count1=sorted(frequency_count.items(),key = lambda item:item[1],reverse=True)
    wordList=[]
    occurenceList=[]
    for i in frequency_count1:
        wordList.append(i[0])
        occurenceList.append(i[1])
    # Give the top 20th words that exists
    plt.bar(wordList[:20],occurenceList[:20])
    plt.show()

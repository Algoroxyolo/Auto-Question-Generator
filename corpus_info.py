import nltk
import collections
import matplotlib.pyplot as plt
def TextOverview(dataset):
    file=open(dataset,mode='r',encoding='utf8')
    textList=[]
    total_list=[]
    content=file.readlines()
    for lines in content:
        punctuations=[',','.','(',')','"','!',"'","[","]","&"]
        for punct in punctuations:
            lines=lines.replace(punct,' ')
        for words in lines.split(): 
            word_token = nltk.word_tokenize(text=words)
            #disgard reoccuring words
            textList=textList+word_token
            textList=list(set(textList))
            #print(wordlist)
            #calculate total word count
            total_list=total_list+word_token

    #find the occurence of each word and find the most frequent occuring one
    frequency_count=collections.Counter(total_list)

    #find the frequency of words of each one
    value=frequency_count.values()
    word_count_dict_temp = collections.Counter(value)
    word_count_items = sorted(word_count_dict_temp.items(),key = lambda item:item[0])
    word_count =[]
    word_number_count = []
    for i in word_count_items:
        word_count.append(i[0])
        word_number_count += textList

    # Give the top 20th words that exists
    plt.bar(word_number_count[:20],word_count[:20] )
    plt.show()

def main(dir,lst):
    for i in lst:
        TextOverview(dir+'/'+i)

main('data/noun_counting_data/',["a1.txt","a2.txt"])


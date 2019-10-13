# Task(a): Reading data from file
f= open('nlp_input.txt','r')
input=f.read()

import nltk
nltk.download('punkt')


# Task(b): Tokenize the text into words and apply lemmatization technique on each word.


# Tokenizing into words
wordTokens = nltk.word_tokenize(input)
print("----Task(b):Tokenize the text into words and apply lemmatization technique on each word.\n")
for wt in wordTokens:
    print(wt)
print("\n")


# Lemmatization
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
for wordTokens in wordTokens:
    print(lemmatizer.lemmatize(wordTokens))
print("\n")


# Task(c): Trigram
triDic = {}
count =1
trigrams = nltk.trigrams(input.split())
print("----Task(c): Trigram\n")
for item in trigrams:
    dicKey=' '.join(item)
    # print(dicKey)
    if dicKey in triDic.keys():
        triDic.update({dicKey:triDic[dicKey]+1})
    else:
        triDic[dicKey]=1
print(triDic,"\n")

# Method-1 to get top 10 values from dictionary
# from collections import Counter
#
# k=Counter(triDic)
# top10 = k.most_common(10)
#
# for i in top10:
#     print(i[0], " :", i[1], " ")

#Task(d)
# Method-2 to get top 10 values from dictionary
from heapq import nlargest

TenHighest = nlargest(10, triDic, key=triDic.get)

print("----Task(d):Dictionary with 10 highest values:")
for val in TenHighest:
    print(val, ":", triDic.get(val))
print("\n")

#Task(e & f ): Tokenizing into sentence and Find all the sentences with the most repeated tri-grams
# Task (g & h): Extract those sentences and concatenate and print the concatenated result

dsfs= "we need to"
sentTokens = nltk.sent_tokenize(input)
maxValue = max(triDic, key=triDic.get)
concatenatedString=''
print("Task(e,f) Combined")
print("----All the sentences with the most repeated tri-grams----\n")
for stok in sentTokens:
    if maxValue in stok:
       print(stok)
       concatenatedString = concatenatedString+stok
print("\n")
print("Task(g,h) Combined")
print("----Concatenated Result----\n")
print(concatenatedString)


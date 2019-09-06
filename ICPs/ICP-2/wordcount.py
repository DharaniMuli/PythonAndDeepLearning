# f = open("sample.txt","r")
#
# worddic ={}
# words = []
# count=0
# for i in f.read().split():
#     words.append(i)
# print(words)
# for word in words:
#     try:
#         worddic.update({word:worddic[word]+1})
#     except:
#         worddic[word] = 1
#
#
# print(worddic)

f = open("sample.txt","r")
outputfile = open("output.txt","w")

worddic ={}
words = []
count=0
for i in f.read().split():
    words.append(i)
print(words)
for word in words:
    if word in worddic.keys():
        worddic.update({word:worddic[word]+1})
    else:
        worddic.update({word:1})

print(worddic)
# outputfile.write(str(worddic))

for k,v in worddic.items():
    outputfile.write("{} {} \n".format(k,v))
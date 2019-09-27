mainStr= "ababcdxa"
mainStrLength= len(mainStr)
resultStr=""
h={}
i=0
j=0
jCount=0
max_length= 0
temp_length=0

for i in range(mainStrLength):
    for j in range(jCount,mainStrLength):
        if mainStr[j] not in h:
            h[mainStr[j]] = 1
            temp_length= temp_length+1
        else:
            h.clear()
            if temp_length>max_length:
                max_length = temp_length
                start = i
                end= j -1
            else:
                max_length = max_length
            temp_length =0
            jCount=i+1
            break
    if j == mainStrLength:
        break
for i in range(start,end+1):
    resultStr = resultStr+ mainStr[i]
print("Longest Sub String is:",resultStr)
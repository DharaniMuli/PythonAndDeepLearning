
str1= "ababcdxa"
sstr2=""

for i in str1:
   try:
    if(str[i]!= str[i+1]):
        str2 = str2+str[i]
   except:
       print(str2)
print(str2)
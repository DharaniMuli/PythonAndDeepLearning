str= input("Enter string here:")
mylist=[]

for i in str:
    mylist.append(i)
print("List of characters",mylist)
for i in range(0,2):
    mylist.pop(i)
print("Removing of last 2 characters:" ,mylist)
reversedlist = mylist[::-1]
print("Reversed list:",reversedlist)
output = ''.join(reversedlist)
print("Reversed string:",output)


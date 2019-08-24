sentance=input("Enter any sentance:")

word1=input("Enter the word that you wanted to replace:")
word2=input("Enter the word with which you want to replace %s with:" %word1)
output=sentance.replace(word1,word2)
print("Final output:",output)
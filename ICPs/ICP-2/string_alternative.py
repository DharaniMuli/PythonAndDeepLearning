# Write a program that returns every other char of a given string starting with first using a function named “string_alternative”

str2 = ""
def string_alternative(str):
    for i in range(len(str)):
        #This % will gives us character at even number of the string
     if i%2 == 0:
        print(str[i])
       


if __name__ == '__main__':

    str = "Good Evening"
    print("Given input:",str)
    string_alternative(str)
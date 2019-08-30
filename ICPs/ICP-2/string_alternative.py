str2 = ""
def string_alternative(str):
    for i in range(len(str)):
     if i%2 == 0:
        print(str[i])
       


if __name__ == '__main__':

    str = "Good Evening"
    print("Given input:",str)
    string_alternative(str)
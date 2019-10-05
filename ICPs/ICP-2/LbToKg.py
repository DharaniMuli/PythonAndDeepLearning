#Define list
Weight_Lb = []

#Take input from user to get number of students
n = int(input("Enter number of students:"))

#Taking weight in Lbs from the user and convert into Int as we recieve str from the 'input'
for i in range(1,n):
    weight = int(input("Enter Student {0} :".format(i)))
    # Pushing each Lb into list
    Weight_Lb.append(weight)

print("Student weights list in Lbs",Weight_Lb)

#Converting of Lb to Kg
Weight_Kg =[var*0.453592 for var in Weight_Lb]
print("Students weight list in Kgs",Weight_Kg)



# Practice questions
# x = ['ab', 'cd']
# for i in x:
#     x.append(i.upper())
# print(x)
#
#
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
# else:
#     print(0)
#

#
# x = "abcdef"
# i = "a"
# while i in x:
#     x = x[:-1]
#     print(i, end = " ")
#
#
# x = 'abcd'
# for i in x:
#     print(i)
#     x.upper()

# d = {0, 1, 2}
# for x in d:
#     print(d.add(x))
#
#
# x = 2
# for i in range(x):
#     x += 1
#     print (x)


# for i in range(10):
#     if i == 5:
#         break
#     else:
#         print(i)
# else:
#     print("Here")


# for i in range(5):
#     if i == 5:
#         break
#     else:
#         print(i)
# else:
#     print("Here")




#  a= [0, 1, 2, 3]
# for a[-1] in a:
#     print(a[-1])
#


# str1= "ababcdxa"
# str2=""
#
# arr = ['a','b','c','c']
#
# for i in range(0,int(arr)):
#     print(arr[0:i+1])
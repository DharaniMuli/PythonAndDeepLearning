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





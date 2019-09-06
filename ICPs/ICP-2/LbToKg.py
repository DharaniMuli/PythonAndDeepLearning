Weight_Lb = []
n = int(input("Enter number of students:"))

for i in range(1,n):
    weight = int(input("Enter Student {0} :".format(i)))
    Weight_Lb.append(weight)

print("Student weights list in Lbs",Weight_Lb)

Weight_Kg =[var*0.453592 for var in Weight_Lb]
print("Students weight list in Kgs",Weight_Kg)





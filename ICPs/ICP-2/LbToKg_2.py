#This is the another way to convert Lb to Kg
moredata= "yes"
weights_lb  = []
weights_kg  = []

while moredata[0] == 'y':
    x = int(input("Enter student weights(lbs)  >> "))
    weights_lb.append(x)
    moredata= input("Do u have  more numbers(yes  or no)? ")
print("Student weights list in Lbs ",weights_lb)
weights_kg = [i*0.453592 for i in weights_lb]
print("Student weights list in Kgs",weights_kg)


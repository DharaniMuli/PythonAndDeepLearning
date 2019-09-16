from collections import defaultdict
mydic = defaultdict(list)

mylist= [('John',('Physics',80)),
         ('Daniel',('Science',90)),
         ('John',('Science',95)),
         ('Mark',('Maths',100)),
         ('Daniel',('History',75)),
         ('Mark',('Social',95))]

for i in range(len(mylist)):

        mydic[mylist[i][0]].append(mylist[i][1])
    
 
print(mydic)



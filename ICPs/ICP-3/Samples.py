class student:
    def __init__(self, n, a):
        self.name = n
        self.age=a

    def get_age(abe):
        age=233
        if(abe.age != age):
            print(age)



s1 = student("Rani",20)
s1.get_age()


class counter:
    overall_counter= 0
    def __init__(self):
        self.my_total=0

    def increment(self):
        counter.overall_counter = counter.overall_counter+1
        self.my_total = self.my_total+  1
a =counter()
a.increment()

print(a.overall_counter)
print(a.my_total)
b = counter()
b.increment()
print(b.__class__.overall_counter)
print(b.my_total)

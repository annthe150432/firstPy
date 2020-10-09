import math

name = ["An", 24, 'd', 54.3, "ds", "asc"]
for i in range(0, 5):
    print(name[i])
print()

print (name*2)
print()
#while loop
i=0
print(name)
while (i<len(name)):
    if i%2==1:
        print(name[i])
    i = i+1
print()

name2 = ["asd", "cee", "da", "as"]
name.append(name2)
print(name)
print()

name.extend(name2)
print(name)
print()
#for loop
for i in name:
    print(i)
print()

#Dictionary
StudentCode = {"K1":"A", "K2":"B", "K3":"C", "K4": "D"}
print(StudentCode["K2"])
print()
del StudentCode["K2"]
print(StudentCode)
print()

print(abs(-5))
print()
print(math.sqrt(5))
print()

try:
    a = int('3.2')
    print(a)
    print()
except:
    print("not an int number")
    print()
#function
def func(name):
    i=0
    while (i<len(name)):
        print(name[i])
        i+=1
func(name2)

a = 'this\'s a %d "messsage"'
print(a%5)
print()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age

p = Person("lasd", 6)
a = p.getName()
b = p.getAge()
print(a, end=' ')
print(b)
print()

n = Person (1, 4)
i = n.getName()
j = n.getAge()
print(i, end=' ')
print(j)

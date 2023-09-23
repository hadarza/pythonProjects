from cmath import sqrt
print("hello world")

x = 2
y = x
x = 1
mylist = ("hey","what")
print(y)
print(11 // 2) # החלק השלם

mySet = {1,2,3,4,5}
mySet2 = {1,2,3,4,5}
x = 5
y = x
z = 5
print(x is y)
print(y is z) #internals
print(mySet is mySet2)
print(x in mySet and x+1 not in mySet)

i = 0
while(i < 10):
    print(i)
    i += 1
    if(i ** 2 == 25) :
        break

else:
    print(f"finish in index {i}")    

# 2,4,6
for i in range(2,8,2) :
    print(i)

names = ["hadar","shir","oriya"]
for name in names :
    print(name)

if (x > 0) :
    """
    some error"""
    # head of fun!
    mylist = ("uu")
    print(mylist)
    x = 1
    print(x)
    print("bigger than 1")


def myfunc2():
    print("hey")

def mag(x,y):
    return sqrt(x ** 2 + y ** 2)

def printNames(*names) :
    for name in names :
        print(f"im a name {name}")
print(mag(3,4))
printNames("hadar","shir","oriya","iris","yossi")

myList2 = ["hadar"]
myList2.insert(0,"bob")
myList2.extend(["shir"])
print(myList2)
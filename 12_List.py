# List is mutable

list = [
    "ada",
    "moric",
    "komra",
    "darucini",
    "rosun",
]

list.append("cini")

# list.sort

# list.remove("moric")

# list.reverse()

# list.insert(3, "alu")

# list.pop(2)

for x in list:
    print(x)

print(list)

####

mylist = ["apple", "banana", "cherry"]

yourlist = ["kathal", "peyara", "lotkon"]

# mylist.extend(yourlist)
mylist.extend(yourlist[0:1])
print(mylist)

mylist.sort(reverse=True)
print(mylist)

def myfunc(m):
    return abs(n - 50)

mylist.sort(key=myfunc)

print(mylist)


#### can extend from tuple

mylist2 = ["apple", "banana", "cherry"]

yourtuple = ["kathal", "peyara", "lotkon", "licu"]

# mylist.extend(yourlist)
mylist2.extend(yourtuple)
print(mylist2)

###

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
nfruits = []
for x in fruits:
    if "a" in x:
        nfruits.append(x)

print(nfruits)

newfruits = [x for x in fruits if "a" in x]
print(newfruits)

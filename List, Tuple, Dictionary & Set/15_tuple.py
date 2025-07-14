fd = (
    1,
    2,
    2,
    2,
    3,
)

# print(fd.count(2))

print(fd.index(3))

print(fd)


x = ("apple", "banana", "cherry")

y = list(x)
y[1] = "licu"
x = tuple(y)

print(x)


mytuple = ("apple", "banana", "cherry")
yourtuple = ("licu",)

mytuple += yourtuple

print(mytuple)

# del mytuple
# print(mytuple) # retun an error

print("\n")
###

yourntuple = ("apple", "banana", "cherry", "licu")

(nofol1, nofol2, nofol3, nofol4) = yourntuple

print(nofol1, nofol2, nofol3, nofol4)

print("\n")
###

myntuple = ("apple", "banana", "cherry", "licu", "jaam")

(fol1, fol2, fol3, *fol4) = myntuple

print(fol1, fol2, fol3)
print(fol4)

print("\n")
###

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, blue, *tropic, red) = fruits

print(green)
print(blue)
print(tropic)
print(red)
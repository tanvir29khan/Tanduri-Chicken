# now i'll learn negative slicing

name = "Tanvir Khan"

print(name[-3:-1])  # Slicing from the third last character to the second last character

print(name[1:3])  # same as name[-3:-1] but using positive indexing

print(name[:3])  # same as name[0:3] but using slicing from the start

print(name[3:])  # same as name[3:len(name)] but using slicing to the end

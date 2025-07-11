foods = set()

foods.add(18)
foods.add("18")
print(foods)

theSet = set((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # using set() constructor to create a set
print(theSet)

thisset = {"apple", "banana", "cherry", "komolalebu"}

for x in thisset:
    print(x)

print("\n") # for new line
print("cherry" in thisset)

print("\n") # for new line
print("cherry" not in thisset)

thisset.add("orange") # adding an item to a set
print(thisset)

thisset.update(["kiwi", "orange"]) # updating a set with multiple items
print(thisset)

print("\n") # for new line
thisset.remove("banana") # removing an item from a set

# thisset.remove("kola") # it will ocur error beacuse item is not present

thisset.discard("amruz") # removing an item from a set without error if item is not present
print(thisset)

thisset.pop() # removing a random item from a set
print(thisset)


yam_set = {"yam", "potato", "cassava", "rice"}

yam_set2 = {"yam", "potato", "kola", "sobji", "yam"}

yam_set3 = yam_set.union(yam_set2) # union of two sets
print(yam_set3)

yam_set4 = yam_set.intersection(yam_set2) # intersection of two sets
print(yam_set4)



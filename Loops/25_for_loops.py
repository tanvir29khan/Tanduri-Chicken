# this is for loops

# for number in range(50):
#     print(number)

list = ["hero", 2, "zero", 4, "to", 5]

# for gg in range(len(list)):
#     print(list[gg])

for item in list:
    print(item)

else:
    print("Loop ended")

print("\nIt's time for continue")
for item in list:
    if item == "zero":
        continue
    print(item)

print("\nNow time for break")
for item in list:
    if item == "zero":
        break
    print(item)

print("\nNow time for pass")
for item in list:
    if item == "zero":
        pass
    print(item)

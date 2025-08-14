MyList = [
    78,
    47,
    657,
    44,
    84,
    56,
    874,
    17,
    758,
    7865,
    8375,
    67,
    573,
    675,
    4857,
    67,
    5784,
    75,
    82,
    19,
    903,
    898,
    23,
]

lowValu = MyList[0]

for i in MyList:
    if i < lowValu:
        lowValu = i

print(f"Lowest Value form this list is {lowValu}")
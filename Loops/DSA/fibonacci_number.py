# this is my own solving problem
a = 0
b = 1

print(a)
for i in range(5):
    c = a + b
    print(c)
    a = b
    b = c

print("\n")  # new line

# now i'll using recursion
print(0)
count = 1


def febonacci(num1, num2):
    global count
    if count <= 5:
        newNum = num1 + num2
        print(newNum)
        num1 = num2
        num2 = newNum
        count += 1
        febonacci(num1, num2)

    else:
        return


febonacci(0, 1)

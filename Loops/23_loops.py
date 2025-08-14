# for i in range(10000788):
#     print(i)


# i = 0

# while i <= 100:
#     print(i)
#     i += 1


# i = 100

# while i >= 1:
#     print (i)
#     i -= 1


# for i in range(100, 0, -1):
#     print(i)

# n = int(input(" enter your number : "))
# x = 0

# for i in range(1, n + 1):
#     x += i
#     # print (x)

# print(x)


# n = int(input(" enter your number : "))
# x = 0
# i = 1

# while i <= n:
#     x += i
#     i += 1

# print(x)

# n = int(input(" enter your number : "))
# x = 1
# i = 1

# while i <= n:
#     x *= i
#     i += 1

# print(x)


# n = int(input(" enter your number : "))
# x = 1

# for i in range(1, n+1):
#     x *= i

# print(x)


n = int(input("Enter your number: "))

for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1))

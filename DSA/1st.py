n = int(input("enter your number: "))

num = n

# count = 0

# while num > 0:
#     count += 1
#     num = num // 10
#     # print(num)
# print(count)


from math import log10


def digitsCount(num):
    return print(int(log10(num)) +1)

digitsCount(num)
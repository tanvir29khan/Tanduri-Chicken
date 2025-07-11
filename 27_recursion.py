def num(n):
    if n == 0:
        return
    print(n)
    num(n - 1)


# a = int(input("enter a number: "))
# num(a)


def fact(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return fact(n - 1) * n


# print(fact(5))


def sum(n):
    if n == 0:
        return 0
    else:
        return sum(n - 1) + n


# print(sum(5))

mist = ["Janna", "Hamma", "Khani", 56, True, "etc"]


def list(l, x=0):
    if x == len(l):
        return
    print(l[x])
    list(l, x + 1)


list(mist)

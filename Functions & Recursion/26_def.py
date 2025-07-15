def welcome(name, /, msg="Hi"):
    print(f"{msg}, {name}.")


def welcame(*, name, msg="Hi"):
    print(f"{msg}, {name}.")


welcame(name="Chicken",)
welcome("Tanduri", msg="hellow")


# mist = ["jibon",'janina','manina','duru kemane','to kise','meeeeen']

# def print_list_len(list):
#     for i in list:
#         print(i , end = ' ')

# print_list_len(mist)


# now i'll make a function to find a number factorial

# def factorial(n):
#     x = 1
#     for i in range(1 , n+1):
#         x = x * i
#     print (x)


# factorial(5)


# i'll concert USD to BDT
# a = int(input("$USD = "))

# def usdTobdt(usd):
#     teka = usd*121.91
#     print("৳BDT =",teka)

# usdTobdt(a)


# a = int(input("Enter a number: "))

# def eve_odd_finderJ(num):
#     if num%2 == 0:
#         print (f"{num} is Even")
#     else:
#         print(f"{num} is Odd")

# eve_odd_finderJ(a)

x = "Tanvir Khan"  # 🔵 Global variable


def mytanvir():
    x = "The men is"  # 🟠 Local variable (inside function)
    print(x)


mytanvir()  # 👉 prints the local 'x'
print(x)  # 👉 prints the global 'x'


score = 3


def increase_score():
    global score
    score += 10


increase_score()
print(score)  # Output: 13
text = "Python is awesome"
words = text.split()

print("Split: ", words)

joined = "-".join(words)
print(joined)

csv = "apple,banana,mango"
print("CSV Split:", csv.split(","))

limited = "a b c d e".split(" ", 2)
print("Maxsplit: ", limited)

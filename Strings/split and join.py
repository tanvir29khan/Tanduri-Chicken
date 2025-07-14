# split examples:

print("hello world python".split())  # → ['hello', 'world', 'python']

print("one|two|three".split("|"))  # → ['one', 'two', 'three']

print("2025-05-26".split("-"))  # → ['2025', '05', '26']

print("a b c d e".split(" ", 2))  # → ['a', 'b', 'c d e']

# join examples:

print(",".join(["a", "b", "c"]))  # → 'a,b,c'

print(" ".join(["hello", "world"]))  # → 'hello world'

print("\n".join(["line1", "line2", "line3"]))

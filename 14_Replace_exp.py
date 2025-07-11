letter = """
Dear <|Name|>,
You are selected!
<|Date|>
"""

name = input("Type your beautiful name: ")
date = input("Type todays date full(24/02/25): ")

final = letter.replace("<|Name|>", name).replace("<|Date|>", date)

print(final)

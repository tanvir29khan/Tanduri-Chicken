blank_list = []

n = int(input("Enter your number list legth : "))

for i in range(n):
    num = int(input(f"{i+1} no. number : "))
    blank_list.append(num)

high = max(blank_list)

print(f"Highest number is {high}")

# print(blank_list)





# this is from AI. After using my brain i found this from AI




# Method 1: Taking numbers one by one until user stops
def find_max_from_input():
    numbers = []
    print("Enter numbers one by one. Type 'done' when finished:")
    
    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number or 'done' to finish.")
    
    if numbers:
        print(f"The highest number entered is: {max(numbers)}")
    else:
        print("No numbers were entered.")

# Call the function
find_max_from_input()


# Method 2: Taking all numbers at once separated by spaces
def find_max_from_single_input():
    user_input = input("Enter numbers separated by spaces: ")
    try:
        numbers = [float(num) for num in user_input.split()]
        if numbers:
            print(f"The highest number entered is: {max(numbers)}")
        else:
            print("No numbers were entered.")
    except ValueError:
        print("Please enter valid numbers separated by spaces.")

# Call the function
find_max_from_single_input()


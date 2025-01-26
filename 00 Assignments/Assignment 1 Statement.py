name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Welcome, {name}!")

# Validate the age
if age <= 0:
    print("Error: Age must be greater than 0.")
    exit()

# Voting eligibility check
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

number = int(input("Enter a number between 1 and 100: "))

# Sum of numbers divisible by the input number
if 1 <= number <= 100:
    total = sum(i for i in range(1, 101) if i % number == 0)
    print(f"The sum of all numbers divisible by {number} from 1 to 100 is: {total}")
else:
    print("Error: The number must be between 1 and 100.")

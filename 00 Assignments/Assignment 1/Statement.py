# Assignment 1: Write a Python program that:
# Takes the following inputs from the user:
# Name (string)
# Age (integer)
# A number between 1 and 100 (integer)
# Performs the following tasks:
# Check if the age entered is valid (greater than 0). If not, print an error message and exit.
# Print a welcome message using the user's name.
# Calculate the sum of all numbers divisible by the input number (from 1 to 100), and display the result.
# Extra functionality:
# If the user's age is 18 or more, print "You are eligible to vote." Otherwise, print "You are not eligible to vote."


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

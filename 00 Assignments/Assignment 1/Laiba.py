# Assignment 1: Write a Python program that:
# Takes the following inputs from the user:
# Name (string)
# Age (integer)
# A number between 1 and 100 (integer)
# Performs the following tasks:

name = input("Enter your name: ")
age = int(input("Enter your age: "))
input_n = int(input("Enter a number between 1 and 100: "))

# Check if the age entered is valid (greater than 0). If not, print an error message and exit.

if age > 0:
    print("Valid Age!")
else:
    print("Not Valid!")

# Print a welcome message using the user's name.

print("Welcome!", name)

# Calculate the sum of all numbers divisible by the input number (from 1 to 100), and display the result.

if 1 <= input_n <= 100:
    total = 0
    for n in range(1, 100):
        if n % input_n == 0:
            total += n
    print("The sum of all numbers from 1 to 100 that are divisible by %d is:%d" %(input_n,total) )
else:
    print("Error!")

# Extra functionality:
# If the user's age is 18 or more, print "You are eligible to vote." Otherwise, print "You are not eligible to vote."

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

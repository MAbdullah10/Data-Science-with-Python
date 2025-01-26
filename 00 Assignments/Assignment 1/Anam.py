# Assignment 1: Write a Python program that:
# Takes the following inputs from the user:
# 1 Name (string)
# 2 Age (integer)
# 3 A number between 1 and 100 (integer)
# Performs the following tasks:
# 1 Check if the age entered is valid (greater than 0). If not, print an error message and exit.
# 2 Print a welcome message using the user's name.
# 3 Calculate the sum of all numbers divisible by the input number (from 1 to 100), and display the result.
# - Extra functionality:
# If the user's age is 18 or more, print "You are eligible to vote." Otherwise, print "You are not eligible to vote."

# Anam Bhutta
import sys

name = input ("Enter your name: ")
age = int(input ("Enter your age: ")) 
if(age<=0):
    print("--- Invalid age! ---")
    sys.exit()
num = int(input ("Enter a number (1 to 100): "))

print("Welcome aboard ",name,"!")

sum = 0
for x in range(1,100):
    if(x%num==0):
        sum=sum+x 
print("The sum of all numbers divisible by ", num, " = ",sum)

if(age>=18):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
#Anam Bhutta

# Task 1: Tuple Practice
# Create a tuple containing the names of 5 of your favorite fruits.
# Print the second and fourth fruits from the tuple.
# Try modifying one of the elements of the tuple (observe and note the error).
# Convert the tuple into a list, add a new fruit to the list, and then convert it back into a tuple. Print the modified tuple.

fruits = ("Orange", "Mango", "Grapes", "Peach", "Cherry")
print("Second and fourth fruits: ", fruits[1],fruits[3])

#fruits.remove("Peach")         #AttributeError: 'tuple' object has no attribute 'remove'
#fruits[1] = "Banana"           #TypeError: 'tuple' object does not support item assignment

fruitList = list(fruits)
fruitList.append("Banana")
fruits = tuple(fruitList)
print("Tuple after modification: ", fruits)

# Task 2: List Practice
# Create a list of 8 random numbers.
# Sort the list in ascending order and print it.
# Add two new numbers to the list and print the updated list.
# Remove the first occurrence of a specific number from the list.
# Reverse the list and print it.

num =[3,6,4,2,6,1,9,10]
print("Original list: ", num)

num.sort()
print("Sorted List: ",num)

num.append(19)
num.append(5)
print("List with two new numbers:",num)

num.remove(6)
num.reverse()
print("Reversed list: ",num)

# Task 3: Dictionary Practice
# Create a dictionary where keys are student names and values are their scores in a test. (At least 5 entries).
# Add a new student and their score to the dictionary.
# Update the score of an existing student.
# Remove one student from the dictionary.
# Print all the keys and values separately.

std = {"Ali":82, "Ahmad":68, "Abdullah":76, "Saad":89, "Hassan":80, "Haadi":78}
print(std)

std.update({"Qasim":85})
print("New student added: ", std)

std.update({"Ali":92})
print("Updated Ali's marks: ", std)

std.pop("Ahmad")

print("Keys: ",std.keys())
print("Values: ",std.values())

# Task 4: Set Practice
# Create a set of 6 unique colors.
# Add two new colors to the set.
# Try adding a duplicate color and observe what happens.
# Remove a specific color from the set.
# Find the union and intersection of this set with another set of 4 colors.

colors = {"Lilac", "Maroon", "Black", "Navy Blue", "Green", "Baby Pink"}
print("Colors Set: ", colors)

colors.add("Yellow")
colors.add("Grey")
print("Colors Set with 2 new colors: ", colors)

colors.add("Lilac")
print("Duplicate value(lilac): ", colors)  #Didn't print the duplicate value

colors.remove("Yellow")
print("Colors Set after removing Yellow: ", colors)

colors2 = {"Orange", "Neon", "Black", "Red"}
print("Intersection of both sets: ", colors.intersection(colors2))
print("Union of both sets: ", colors.union(colors2))



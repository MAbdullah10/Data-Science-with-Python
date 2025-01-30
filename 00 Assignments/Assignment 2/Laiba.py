# Task 1: Tuple Practice
# Create a tuple containing the names of 5 of your favorite fruits.
# Print the second and fourth fruits from the tuple.
# Try modifying one of the elements of the tuple (observe and note the error).
# Convert the tuple into a list, add a new fruit to the list, and then convert it back into a tuple. Print the modified tuple.

fruits = ("Apple", "Banana", "Mango", "Orange", "Guava")

print("Second element of tuple:")
print(fruits[1])

print("Fourth element of tuple:")
print(fruits[3])

#list
y = list(fruits)
y[1] = "Grapes"
fruits = tuple(y)

print(fruits)

# Task 2: List Practice
# Create a list of 8 random numbers.
# Sort the list in ascending order and print it.
# Add two new numbers to the list and print the updated list.
# Remove the first occurrence of a specific number from the list.
# Reverse the list and print it.


list = [24, 59, 12, 36, 84, 48, 60, 72]
print(list)
list.sort()
print(list)

list.append(99)
print(list)

list.append(83)
print(list)

list.remove(59)
print(list)

list.reverse()
print(list)

# Task 3: Dictionary Practice
# Create a dictionary where keys are student names and values are their scores in a test. (At least 5 entries).
# Add a new student and their score to the dictionary.
# Update the score of an existing student.
# Remove one student from the dictionary.
# Print all the keys and values separately.

dictionary = {"Laiba":42,"Anam":40,"Abdullah":38,"Noor":30,"Ahmed":45 }
print(dictionary)

dictionary.update ({"Amaaz":29})
print(dictionary)

dictionary["Noor"] = 37
print(dictionary)

dictionary.pop("Ahmed")
print(dictionary)

key = dictionary.keys()
print(key)

value = dictionary.values()
print(value)

# Task 4: Set Practice
# Create a set of 6 unique colors.
# Add two new colors to the set.
# Try adding a duplicate color and observe what happens.
# Remove a specific color from the set.
# Find the union and intersection of this set with another set of 4 colors.

col = {"Red", "Yellow", "Blue", "Green", "Black", "Orange"}
print(col)

col.add("Purple")
print(col)

col.add("White")
print(col)

col.add("Red")
print(col)  

col.remove("Yellow")
print(col)

col1 = {"Purple", "Red", "Pink", "Blue"}
print(col.union(col1))
print(col.intersection(col1))
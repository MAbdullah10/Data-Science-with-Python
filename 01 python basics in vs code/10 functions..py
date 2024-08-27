print("Learning python")
print("Learning python")
print("Learning python")
print("Learning python")
print("Learning python")

#instead of above we'll use a function
#Method 1
def print_func():
    print("Learning python")
    print("Learning python")
    print("Learning python")

print_func()

#Method 2
def print_func():
    text = "we are trying the second way (edited)"
    print(text)
    print(text)
    print(text)    
    
print_func()

#Method 3
def print_func(text):
    print(text)
    print(text)
    print(text)    
    
print_func("That's the third way ")

#Defining func with if,elif statements
def school_calc(age,name):
    if age == 5:
        print(name, " can go to school")
    elif age > 5:
        print(name, " can go to higher school")
    else:
        print(name," can't go to school")

school_calc(2,"Ali")


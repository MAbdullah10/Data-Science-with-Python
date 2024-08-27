x = 10      #integer
y = 10.2    #float
z = "Hello" #string

#Implicit type conversion
x = x*y     #int*float = float
print(x," type of x is ",type(x))

#Explicit type conversion
age = input("What's your age? ")
print(type(age))
age = int (age)
print (age, "type of age is ",type(age))


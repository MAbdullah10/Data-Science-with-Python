#While Loop
x = 0
while(x<5):
    print(x) 
    x = x+1

#For Loop
for x in range(5,10):
    print(x)

#array
days = ["Mon", "Tue","Wed","Thurs","Fri","Sat","Sun"]
for d in days:
    if (d=="Thurs"):break   #loop stops and exists
    if (d=="Thurs"):continue#it will skip this value
    print(d)
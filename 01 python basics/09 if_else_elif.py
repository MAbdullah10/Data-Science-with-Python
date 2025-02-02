required_age_at_school = 5
ali_age = 6

std_name = input ("Name: ")
std_age = input("Enter your age: ")
std_age = int(std_age)

#question: can ali go to school
if std_age == required_age_at_school:
    print(std_name,"can go to school")
elif std_age>required_age_at_school:
     print(std_name,"should go to higher secondary school")
else:
    print(std_name," cannot go to school")
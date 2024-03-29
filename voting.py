# Nested if : 

citizen = "american"
age = 67

if(citizen=="indian"):
    if(age>18 and age<105):
        print("Eligible to vote")
    else:
        print("Required Age Unsatisfied")
else:
    print("Not a citizen of India")
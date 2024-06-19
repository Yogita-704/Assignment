#Ques13: Write a program that asks the user for their birth year and calculates their age.
year=int(input("Enter your birth year:"))
recent_year=int(input("Enter recent year:"))
age=0
while 1:
    age=age+1
    year=year+1
    if year==recent_year:
        print("Your age is:",age)
        break
    else:
        pass



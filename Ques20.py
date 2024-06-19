#Ques20: Write a python program that takes a list of numbers and returns their sum
num1=int(input("Enter a number:"))
sum=0
sum=sum+num1
while 1:
    option=input("Enter you want to add next number or not:")
    if option.lower()=="yes":
        num2=int(input("Enter next number:"))
        sum=sum+num2
    else:
        break
print("The sum of given numbers is:",sum)


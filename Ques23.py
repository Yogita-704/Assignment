#Ques23: Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
temp=int(input("Enter the temperature: "))
choice=input("Enter you want to convert temperature in Celsius or Fahrenheit:")
if choice.lower()=="celsius":
     temp=(temp-32)*(5/9)
     print("The Temperature is:",temp,"°C")   #°C = (°F - 32) × 5/9
elif choice.lower()=="fahrenheit":
     temp=(temp*(9/5))+32 #°F = (°C × 9/5) + 32
     print("The Temperature is:", temp, "°F")
else:
     print("Check You have entered something wrong in choice ")
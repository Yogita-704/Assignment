#Ques5: Write a program that takes a string input from the user and writes it to a text file.

str=input("Enter a String you want to print:")
samplefile=open("C:/Users/Yogita/Desktop/Python and Machine learning/Demo.txt",'w')
print(str,file=samplefile)
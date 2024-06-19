#Ques25: Write a program that copies the contents of one text file to another.
samplefile1=open("C:/Users/Yogita/Desktop/Python and Machine learning/Read.txt","r")
samplefile2=open("C:/Users/Yogita/Desktop/Python and Machine learning/Demo.txt","w")
print(samplefile1.read(),file=samplefile2)
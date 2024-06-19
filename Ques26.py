#Ques26: Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
str=input("Enter a string:")
prefix=input("Enter a prefix to check its presence in string:")
suffix=input("Enter a suffix to check its presence in string:")
while 1:
    if str.startswith(prefix):
        print("Yes ",str," starts with prefix ",prefix)
        break
    else:
        print("There is no  given prefix in ", str)
        break
while 1:
    if str.endswith(suffix):
        print("Yes ",str," ends with suffix ",suffix)
        break
    else:
        print("There is no  given suffix in ", str)
        break

    

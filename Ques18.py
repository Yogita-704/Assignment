#Ques18: Write a python program that checks if two strings are anagrams of each other.
str1=input("Enter string1:")
str2=input("Enter string2:")
str1=str1.lower()
str2=str2.lower()
if len(str1)==len(str2):
    sorted_str1=sorted(str1)
    sorted_str2=sorted(str2)
    if sorted_str1==sorted_str2:
        print("Yes, ",str1, " and ",str2," are anagrams of each other")
    else:
        print("No, ",str1, " and ",str2," are not anagrams of each other")
else:
    print("No, ",str1, " and ",str2," are not anagrams of each other")

#Write a program to check if a given string is a palindrome? 
def isPalidrome(str):
   
    for i in range(0,int (len(str))):
        if str[i] !=str [len(str)-i-1]:
            return False
    return True

s="North india"
ans=isPalidrome(s)

if (ans):
     print ("Yes")

else:
     print("no")
#5.) Write a program to check whether a character is an alphabet or not.
#  whether charcter entered is a-z or A-Z or not ?

chr=input("please Enter Charactor :")
if  (ord(chr)>=65 and ord(chr) <=90) or (ord(chr) >= 97 and (ord(chr) <=122)): 
    print (" charactor" , chr, " is a Alphabet")
else:
    print ("this is not a Alphabet")


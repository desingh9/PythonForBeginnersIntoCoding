#1.) Write a program to check whether a entered character is lowercase ( a to z ) or uppercase ( A to Z ).

chr=(input("Enter Charactor:")) #chr for ASCII coding output 
if (ord(chr) >=65 and ord(chr)<=90): #ord to give output in string,65 to 90 used for Upper case 
    print("its a CAPITAL Letter")
elif (ord(chr)>=97 and ord(chr)<=122): #ASCII code 97 to 122 used for Small letters
    print ("its a Small charector")
else:
    print("out of Range ")
#1.) Write a program to check whether a entered character is lowercase ( a to z ) or uppercase ( A to Z ).

chr=(input("Enter Charactor:"))
#A=chr(65,90)
#for i in range(65,90)
if (ord(chr) >=65 and ord(chr)<=90):
    print("its a CAPITAL Letter")
elif (ord(chr)>=97 and ord(chr)<=122):
    print ("its a Small charector")
else:
    print("errrrr404")
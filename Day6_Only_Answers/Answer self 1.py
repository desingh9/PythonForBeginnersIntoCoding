age = int(input("enter your age \n "))
sex = input("enter your sex \n")
#sex=="Famele"
#sex=="male"
if (sex=="Female") and (age <=60):
    print ("you can work in urban area only ")
elif (sex=="Male") and (age>=20 and age<40):
    print ( "you can work anywhere")
elif (sex=="Male") and (age<=60) and (age>40):
    print ("you can work in urban area only2")
else:
    print ("Error")
    
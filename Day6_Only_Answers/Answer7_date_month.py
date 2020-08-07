#7.) Write a Program to print a number of days in month without using any inbuilt library. 
#User will enter the month: 7 , output: 31 days .#Take assumption that month 2 that is feB will have 28 only. 
# as we are not asking year here. so assume the month day to be 28.

m=int(input("Pleaes enter the month number"))
#daysofmonths = ("Jan","Mar", "May", "Jul", "Aug", "Oct","Dec")

List=[1,3,5,7,8,10,12]
if m==2:
    print ("no of days in February 28 or 29")
elif m in List:
    print ("no of days are 31 in this month")
elif m==4 or m==6 or m==9 or m==11:
    print ("days in month is 30")
else:
    print ("invalid input please try again")
    
#7.) Write a Program to print a number of days in month without using any inbuilt library. 
#User will enter the month: 7 , output: 31 days .#Take assumption that month 2 that is feB will have 28 only. 
# as we are not asking year here. so assume the month day to be 28.

month=input("Pleaes enter the month")

def numberOfDays( m):
list = [1,3,5,7,8,10,12]
if m==2:
    print (28)
if m in list:
    print ( " No. of Days in Month is 31")
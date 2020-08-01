A=int(input("enter your Selling price "))
B=int(input("enter your COST Price"))

if A > B:
    print (f"you got profit on the item {A-B}")
elif (B>A):  
    print (f"your got losss {B-A}")

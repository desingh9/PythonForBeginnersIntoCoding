#Print a table using while loop 
x=int(input("enter the number : ")) #input
table=1
while table <=10: #enter the range required to print
    print (f"{x}  x {table} = {table * x}" ) #format as output needed
    table+=1
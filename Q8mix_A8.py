#8)	Write a program to print the following pattern using for loop <br>
#5 4 3 2 1 <br>
#4 3 2 1 <br>
#3 2 1 <br>
#2 1 <br>
#1<br>

i=int(input("enter the nuber to print row :"))

for a in range (i):
    for z in range (a,i):

        print ( 6-z ,end=" ")
    print("<br>")

"""6)	Write a program to print the following pattern<br>
1<br>
1 2<br>
1 2 3<br>
1 2 3 4<br>
1 2 3 4 5<br>"""

x=int(input("enter the nuber to print row :"))

for x in range (1, x):
    for y in range (x):

        print (x,end=" ")
    print()
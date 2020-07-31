#Given the length and breadth of a rectangle, 
#write a program to find whether the area of the rectangle is greater than its perimeter. 
#<br>For example,
#the area of the rectangle with length = 5 and breadth = 4 is greater than its perimeter.
length=int(input("enter the length "))
breadth=int(input("enter the breadth "))
area=(length*breadth)
perimeter=int(2*(length+breadth))
if perimeter>area:
    print(f"perimenter is greater {perimeter}")
elif area>perimeter:
    print(f"area is Greater")
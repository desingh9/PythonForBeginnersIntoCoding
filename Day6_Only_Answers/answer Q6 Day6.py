#Q=7 Given a point (x, y), write a program to find out if it lies on the x-axis, 
# y-axis or at the origin, viz. (0, 0).
x=int(input("enter the point in \"x\""))  #Variable
y=int(input("enter the point in \"y\"")) #Variable
#int(input("Enter the point{x.y}"))
if (x==0 and y==0):
    print("Point lies on the Origin\n")
elif(x==0):
    print("point lies on y- axis")
elif(y==0):
    print("point lies on x- axis")
else:
    print ("Error")

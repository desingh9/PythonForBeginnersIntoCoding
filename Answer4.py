#4.) Write a program to check whether triangle is equilateral, scalene or isosceles
        Isosceles triangle: In geometry, an isosceles triangle is a triangle that has two sides of equal length.
        Equilateral triangle: In geometry, an equilateral triangle is a triangle in which all three sides are equal.
        Scalene triangle: A scalene triangle is a triangle that has three unequal sides.

input ("enter the length of triangle sides: ")
x=int ( input ("x: " ))
y=int (input ("y :"))
z=int (input("z :"))
if x==y==z:
    print ("Equilateral Triangle")
elif x==y or y==z or z==x:
    print('isosceles tiangle')
else:
    print ("scalene triangle")

 

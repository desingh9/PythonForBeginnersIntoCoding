#5. **Isosceles triangle**

 #   Given a number n, print a centered triangle. 
    
  #  Example for n=3:
   #    *
    #  ***
    # *****

n=int(input(" enter the no:"))
for i in range(n):

    #print(" "*(n-i-1),end="")
    #space
    for x in range(n-i-1):
        print(" ",end="")
    #print extra*
    print("#",end="")
    #print star according to no
    for y in range (2*i):
       # print("" ,end=" ")
        print("#",end="" )
    print()
    

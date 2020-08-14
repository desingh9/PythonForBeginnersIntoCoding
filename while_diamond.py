"""5. **Isosceles triangle**

    Given a number n, print a centered triangle. 
    
    Example for n=3:
    ```
      *
     ***
    *****
"""
rows = (6)
for i in range(0, rows):
    for j in range(0, i):
        print (" *" , end = " ")
        #print(" * ", end=' ')
    print("\r")
k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
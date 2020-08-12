"""4. **Draw a right triangle**

    Given a number n, print n lines, each with one more asterisk than the last (i.e. one on the first line, two on the second,etc.) 
    
    Example when n=3:
    ```
    *
    **
    ***"""
for i in range (10):
    for j in range (i):
        print("*" ,end = " ")
    print("")
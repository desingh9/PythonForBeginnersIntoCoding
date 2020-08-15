# a represents the array 
# n : Number of elements in array a 
"""def getMissingNo(a,n): 
	i, total = 0, 1
	for i in range(2,n + 2): 
		total += i 
		total -= a[i - 2] 
	return total 

# Driver Code 
listA = [1, 2, 3, 4, 5 ,6,8,9] 
print("the missing num is " , getMissingNo( listA , len(listA))) 
"""
#method 2
list1 = [1, 2, 3, 4, 5 ,6,8,9]
#x,y,z final value
y=0
z=7
for x in list1:
    if y+(x-1)==z:
        print("the answer is " + str (x-1))

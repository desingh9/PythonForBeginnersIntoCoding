#1)	Write a program to find the missing number in a given integer array of 1 to 100?

# getMissingNo takes list as argument 

def getMissingNo(A): 
	n = len(A) 
	total = (n + 1)*(n + 2)/2
	sum_of_A = sum(A)   
	return total - sum_of_A 
# a represents the array 
# n : Number of elements in array a 
def getMissingNo(a, n): 
	i, total = 0, 1

	for i in range(2, n + 2): 
		total += i 
		total -= a[i - 2] 
	return total 

# Driver Code 
arr = [1, 2, 3, 4,6] 
print("Missing no is ", getMissingNo(arr, len(arr))) 

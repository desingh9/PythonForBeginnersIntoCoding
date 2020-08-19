#1)	Write a program to find All the missing numbers in a given integer array ?

arr = [1, 2,5,,9,3,11,15] 
occurranceOfDigit=[]

# finding max no so that , will create list will index till max no .
max=arr[0]
for no in arr:
    if no>max:
        max=no

# adding all zeros [0] at all indexes till the maximum no in array
for no in range(0,max+1):
    occurranceOfDigit.append(0)

# original array
print(arr)

# marking index in occurrance array to 1 for all no in original array. marking indexes that are present in original array
for no in arr:
    occurranceOfDigit[no]=1 


print("Missing elements  are: ")
i=1
# accesing all indexes where values are zero. i.e  no. are not present in array
while i<=max:
    if occurranceOfDigit[i]==0:
        print(i,end=" ")
    i+=1


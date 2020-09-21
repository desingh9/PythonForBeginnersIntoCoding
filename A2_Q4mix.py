#2)	Write a program to find the duplicate number on a given integer array? 1,3,3,4 =3 or 1929 =9
arr= [0,1,2,3,2,4,5,5,8,8,4]
print ("Duplicate element in given arrey: ")
#Searches for Duplicate elements
for i in range (0,len (arr)):
       for j in range (i+1, len (arr)):
        if (arr[i]== arr[j]):
            print (":" ,arr[j] , end =(" "))
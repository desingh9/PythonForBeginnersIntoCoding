#3)	Write a program to find the largest and smallest number in an unsorted integer array? 

List = []
val=int(input("enter no. of elements : "))
for i in range (val):
    num=int(input('Input value of element :'))
    List.append(num)
max=List[0]
for i in range(val):
    if (List [i])>max:
        max= List[i]
min=List[0]
for i in range(val):
    if (List [i])<min:
        min=List[i]
#print ('max number=' ,max)

print('Index position of smallest element in the list is :' , min)
print('Index position of Biggest element in the list is :' ,max )

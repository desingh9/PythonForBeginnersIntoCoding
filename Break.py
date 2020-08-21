i=2
currentSum=0
maxSum=50

while i<=500:
    if currentSum+i>maxSum:
        break
currentSum=currentSum+i
i=i+1
print (i)
#to display stars in equilateral triangular form

n=11
for i in range (1, 10):
    #print(' '*(n-i) + '* '*(i)) #can be written in below format as well 
    print(' '*n, end='')
    print ('* '*(i))
    n-=1
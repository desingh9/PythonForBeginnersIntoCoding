#2.) Take input of age of 3 people by user and determine oldest and youngest among them.
ages=input("enter the ages of Person with Space")
agesIntList=[]
agesList=ages.split (" ")
for age in agesList:
    agesIntList.append (int(age))    #to convert ages value in integer 

print(" Before " ,agesIntList)
agesIntList.sort()
print(" after " ,agesIntList)

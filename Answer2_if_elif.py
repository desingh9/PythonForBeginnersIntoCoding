#2.) Take input of age of 3 people by user and determine oldest and youngest among them.
ages=input("enter the age of Person with Space")
agesList=[]
agesList=ages.split (" ")
for ages in agesList:
    agesList.append (int)(age) #to convert ages value in integer 
print("Before" ,agesList)
agesList.sort()
print("after" ,ageslist)

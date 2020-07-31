hardness = int (input("Enter the hardness:" ))
carbonContent = int (input("Enter the carbon content:" ))
tensileStrength = int (input("Enter the tensile strength:" ))

def IsCondition1Passed():
    if hardness>50:
        return true
    else:
        return false

def IsCondition2Passed():
    if carbonContent<0.7:
        return true
    else:
        return false

def IsCondition3Passed():
    if tensileStrength>5600:
        return true
    else:
        return false
  
if (IsCondition1Passed and IsCondition2Passed and IsCondition3Passed):
    print ("your Steel Grade is 10")
elif (IsCondition1Passed and IsCondition2Passed):
    print ("your steel Grade is 9")
elif (IsCondition2Passed and IsCondition3Passed):
    print("your Steel Grade is 8")
elif (IsCondition1Passed and IsCondition3Passed):
    print("your Steel Grade is 7")
elif (IsCondition1Passed or IsCondition2Passed or IsCondition3Passed):
    print("your Steel Grade is 6")
else:
    print("your Steel Grade is 5")
#8.) write a program to ask user temperature in celcius or fehrenheit and convert the temperatur in a another format
     #Ex:
        # input:
         #Enter temperature: 40c Output :
         #Hey temperature 40 C  in fehrenheit will be 104 F
         
         #input:
        # Enter temperature: 98.4 F
        # Output :
        # Hey temperature 98.4 F in celcius will be 36.88 C

temprature=input ("Enter the temprature: ")
splitvalue=temprature.split (" ")
#value=splitvalue[1] print(splitvalue [0] ) print(splitvalue [1] )
Celsius,f=0,0
output=f"temprature in f is {f})"
temprature= float(splitvalue [0])
unit=splitvalue[0]
#tempValue=int (splitvalue )
print("temprature in Celsius:" , 'C')
if unit.upper()=='c':
    celsius=temprature
    f=(celsius/1.8 - 32)
    output=f"temprature in f will be {F}"
elif unit.upper()=="F":
    f=temprature
    celsius=(f-32)*1.8
    output=f"temprature in celsius {Celsius}"
else:
    output=("invalid input")
print("output")


 
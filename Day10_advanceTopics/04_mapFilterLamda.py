nos = [9,11,15,19,31]
doubleOfnos = map(lambda no: no*2, nos)

for x in doubleOfnos:
  print(x )

<<<<<<< HEAD
ages = [5, 12, 17, 18, 24, 32, 45]
=======

ages = [5, 12, 17, 18, 24, 32]
>>>>>>> 489b00de01f5914a0986b4f48a3ef624dcb6e8e9
adults = filter(lambda age: age>19, ages)

for x in adults:
  print(x , end = ":")
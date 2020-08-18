nos = [9,11,15,19,31]
doubleOfnos = map(lambda no: no*2, nos)

for x in doubleOfnos:
  print(x )

ages = [5, 12, 17, 18, 24, 32, 45]
adults = filter(lambda age: age>19, ages)

for x in adults:
  print(x , end = ":")
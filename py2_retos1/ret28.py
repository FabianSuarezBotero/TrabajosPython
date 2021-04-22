fila = range(1,11)
columna = range(1,11)

for i in fila:
  for j in columna:
    mult=i*j
    print (i,'*', j,'=', mult)
    if j == 10:
      print("_"*40)

#print ('hola mundo')

archivo = open ('palabras500.csv', encoding='utf-8')

lineas = archivo.readlines()
#Lineas es una lista que tiene las palabras 

archivo.close()

#print (len(lineas))

#print(lineas[0])

#print (lineas)

for i in lineas:
  palabra = i
  if (palabra [-1:-3] == lineas):
    print (palabra)
  
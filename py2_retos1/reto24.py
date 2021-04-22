palabra = input ('Ingrese una palabra para saber si es un palindromo: ')
pal_inv = palabra [::-1]

if palabra == pal_inv:
  print(f'Efectivamente, {palabra} es un palindromo')
else:
  print (f'Lastimosamente, {palabra} no es un palindromo')
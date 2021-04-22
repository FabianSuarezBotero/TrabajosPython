print ('Para calcular el indice de masa corporal se necesitan el peso y la altura.')

peso = int (input('Ingrese su peso en kilogramos: '))
altura = int (input('Ingrese su altura en metros: '))

def imc ():
  a = peso / (altura ** 2)
  return (a)

print('Su indice de masa corporal es: ')
print (imc())


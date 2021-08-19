granos = 0
for i in range (8*8):
  granos += 2**i
  print(i+1, 2**i, granos)
print(f'Se necesitan {2**i,granos} granos para cumplir con la leyenda de los granos de trigo y el ajedrez')
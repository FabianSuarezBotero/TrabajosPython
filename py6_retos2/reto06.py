import random
num_rand = random.randrange(121)

if num_rand > 10 and num_rand < 50:
  print (f'El numero random {num_rand} se encuentra entre 10 y 50')

else:
  if num_rand > 50 and num_rand < 100:
    print (f'El numero random {num_rand} se encuentra entre 50 y 100')
  
  else:
    if  num_rand > 100:
      print (f'El numero random {num_rand} es mayor que 100')

    else:
      if num_rand < 10:
        print (f'El numero random {num_rand} es menor a 10')
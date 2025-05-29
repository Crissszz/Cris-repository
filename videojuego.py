from random import randint



numero1 = int(input("Ingrese el primer numero: "))

numero2 = int(input("Ingrese el segundo numero: "))



while numero2 < numero1:

  print("El primer numero debe ser menor al segundo")

  numero1 = int(input("Ingrese el primer numero: "))

  numero2 = int(input("Ingrese el segundo numero: "))



numero_secreto = randint(1,10)





intento = 1

sigue_jugando = True



print(f"{numero_secreto}")

intento_ingresado = int(input("Ingrese el primer intento: "))

print("Primer intento")

if intento_ingresado == numero_secreto:

  print("Felicitaciones, has ganado en el primer intento: ")

  sigue_jugando = False

elif intento_ingresado > numero_secreto:

  print("El numero que ingresaste es mayor al numero secreto: ")

  intento+=1

else:

  print("El numero que ingresaste es menor al numero secreto: ")

  intento = intento + 1



if sigue_jugando:

  print("Segundo intento")

  intento_ingresado = int(input("Ingrese el segundo intento: "))

  if(intento_ingresado == numero_secreto):

    print("Felicitaciones, ganaste en el segundo intento: ")

    sigue_jugando = False

  elif intento_ingresado > numero_secreto:

    print("El numero que ingresaste es mayor al numero secreto: ")

    intento+=1

  else:

    print("El numero que ingresaste es mayor al numero secreto: ")

    intento+=1



if sigue_jugando:

  print("Tercer intento")

  intento_ingresado = int(input("Ingrese el tercer intento: "))

  if(intento_ingresado == numero_secreto):

    print("Felicitaciones, ganaste en el tercer intento: ")

    sigue_jugando = False

    intento+=1

  else:

    print(f"Perdiste, el numero secreto era : {numero_secreto}")
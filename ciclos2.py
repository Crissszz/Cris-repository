from random import randint

while True:
    n1 = int(input("Ingrese el primer un numero"))
    if n1 == 0:
        break
    n2 = int(input("Ingrese el segundo un numero"))
    if n2 == 0:
        break
    num = randint(n1,n2)
    print (f"El numero aleatorio es:{num}")
    






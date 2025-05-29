numeroIngresado = int(input("Ingrese el numero a sumar: "))
resultado = 0 # Inicializacion
negativo = False

while not negativo:
    if numeroIngresado < 0:
        negativo = True
        break
    resultado = resultado + numeroIngresado
    print(f"El resultado es: {resultado}")
    numeroIngresado = int(input("Ingrese el numero a sumar: "))

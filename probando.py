

print("Contador de Vocales")

texto = input("Introduce un texto: ")

vocales = "AEIOUaeiou"

contador = 0

for letra in texto:
    if letra in vocales:
        contador += 1


print(f"El texto tiene{contador}vocales")




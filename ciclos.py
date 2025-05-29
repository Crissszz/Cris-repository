try:

    resultado = 10/0
except ZeroDivisionError as nombre_de_excepcion:
    print(f"No se puede dividir por cero: {nombre_de_excepcion}")
else:
    print("No se produjo ninguna excepcion")
finally:
    # Codigo a ejecutar siempre, independientemente de si se produjo una excepion
    print("Este bloque se ejecuta siempre")


randint
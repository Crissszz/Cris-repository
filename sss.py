
def calculadora(num1,num2,opcion):
    try:
        if opcion == 1:
            return num1+num2
        elif opcion == 2:
            return num1-num2
        elif opcion == 3:
            return num1*num2
        elif opcion == 4:
            return num1/num2
    except ValueError:
            print("Solo permite valores numericos, intentelo nuevamente")
    except ZeroDivisionError:
            print("No se puede dividir por cero, intentelo nuevamente")
    except TypeError:
            print("Ingrese bien los datos")
 
 resultado = calculadora(1,"hola",1)
print(f"El resultado es : {resultado}")




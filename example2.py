# Funciones de la calculadora
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

# Menú principal
print("Por favor, elige una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Solicitar al usuario que ingrese la opción
opcion = input("Ingresa una opción (1/2/3/4): ")

# Solicitar al usuario que ingrese los números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Realizar la operación seleccionada
if opcion == '1':
    print(num1, "+", num2, "=", suma(num1, num2))

elif opcion == '2':
    print(num1, "-", num2, "=", resta(num1, num2))

elif opcion == '3':
    print(num1, "*", num2, "=", multiplicacion(num1, num2))

elif opcion == '4':
    print(num1, "/", num2, "=", division(num1, num2))

else:
    print("Opción inválida")
# Mi primer programa en Python
print("==========================================")
print("   ¡Bienvenido a tu primer script Python!  ")
print("==========================================")

# Pedir datos al usuario
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}. Vamos a hacer una suma rápida.")

# Operación matemática básica
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    suma = num1 + num2
    print(f"El resultado de sumar {num1} + {num2} es: {suma}")
except ValueError:
    print("Por favor, ingresa números válidos.")

print("------------------------------------------")
print("¡Felicidades! Has ejecutado código Python con éxito.")


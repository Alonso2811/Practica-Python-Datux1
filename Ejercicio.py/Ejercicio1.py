#Escribir Hola mundo 
print("Hola Mundo")

#Saludo con el nombre de entrada desde teclado, input:"Gianmarco", output:"Hola, Gianmarco"
nombre =input("Ingresa tu nombre: ")
print(f"Hola,{nombre}")

#Programa que pida tu edad y muestre si es o no mayor de edad
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("No eres mayor de edad.")

#Programa que pida número entero y muestre si es par o impar 
numero = int(input("Ingresa un número entero: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

#Programa que pida un número entero y calcule la suma de 1 hasta el número ingresado , usando fórmula de números enteros 
numero = int(input("Ingresa un número entero: "))
suma = (numero * (numero + 1)) // 2  # Fórmula para la suma de los primeros n números
print(f"La suma de los números de 1 hasta {numero} es {suma}.")
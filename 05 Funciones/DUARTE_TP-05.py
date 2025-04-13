"""1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal."""
#Definición de funciones  (serán llamadas en cualquier parte del archivo de ser necesarias, pero se crean en cada ejercicio en particular)
def imprimir_hola_mundo():
    print("Hola mundo!")
#Programa
imprimir_hola_mundo()
"""///////////////////////////////////////////////////////////
2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
volver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario."""
#Definición de funciones  (serán llamadas en cualquier parte del archivo de ser necesarias, pero se crean en cada ejercicio en particular)
def saludar_usuario(nombre):
    print (f"Hola {nombre}!")
#Programa
nombre = input("Ingrese su nombre de usuario: ")
saludar_usuario(nombre)
"""/////////////////////////////////////////////////////////////////
3. Crear una función llamada información_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
dir los datos al usuario y llamar a esta función con los valores in-
gresados."""
#Definición de funciones  (serán llamadas en cualquier parte del archivo de ser necesarias, pero se crean en cada ejercicio en particular)
def información_personal(nombre,apellido,edad,residencia):
    print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
#Programa
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")
información_personal(nombre,apellido,edad,residencia)

"""///////////////////////////////////////////////////////////////////
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
dio como parámetro y devuelva el área del círculo. calcular_peri-
metro_circulo(radio) que reciba el radio como parámetro y devuel-
va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
bas funciones para mostrar los resultados."""
#Definición de funciones  (serán llamadas en cualquier parte del archivo de ser necesarias, pero se crean en cada ejercicio en particular)
import math #Se importa de la biblioteca para usar pi
def calcular_area_circulo(radio):
    return pi * (radio*radio)
def calcular_perimetro_circulo(radio):
    return 2* pi * radio
#Programa
pi = math.pi
radio=float(input("Ingrese el radio: "))
print (f"el area del circulo es {calcular_area_circulo(radio)} y el perimetro es {calcular_perimetro_circulo(radio)}")

"""///////////////////////////////////////////////////////////////////
5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mos-
trar el resultado usando esta función."""
#Definición de funciones  (serán llamadas en cualquier parte del archivo de ser necesarias, pero se crean en cada ejercicio en particular)
def segundos_a_horas(segundos):
    return segundos / 3600
#Programa
segundos=int(input("Ingrese la cantidad de segundos: "))
print(f"La cantidad de segundos en horas es {segundos_a_horas(segundos)}")

"""///////////////////////////////////////////////////////////////////
6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la fun-
ción."""
#Definición de funciones  (serán llamadas en cualquier parte del archivo de ser necesarias, pero se crean en cada ejercicio en particular)
def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado= i * numero
        print(f"{i} X {numero}= {resultado}")
#Programa
numero =int(input("ingrese un numero para ver su tabla: "))
tabla_multiplicar(numero)

"""///////////////////////////////////////////////////////////////////
7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resulta-
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
sultados de forma clara."""
#Definición de funciones  (serán llamadas en cualquier parte del archivo de ser necesarias, pero se crean en cada ejercicio en particular)
def operaciones_basicas(a, b):
    suma = a + b
    resta=a-b
    multiplicacion= a*b
    division= a/b
    return suma,resta,multiplicacion,division
#Programa
a=float(input("ingrese un numero: "))
b=float(input("ingrese otro numero: "))
resultados = operaciones_basicas (a,b)
suma, resta,multiplicacion, division = resultados
print(f"la suma de ambos números es: {suma}")
print(f"la resta de ambos números es: {resta}")
print(f"la multiplicacion de ambos números es: {multiplicacion}")
print(f"la division de ambos números es: {division}")

"""///////////////////////////////////////////////////////////////////
8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
ción para mostrar el resultado con dos decimales."""
#Definición de funciones  (serán llamadas en cualquier parte del archivo de ser necesarias, pero se crean en cada ejercicio en particular)
def calcular_imc(peso, altura):
    altura_m=altura /100
    resultado = peso / (altura_m**2)
    return round (resultado,2)
#Programa
peso=float(input("Ingrese su peso en Kg: "))
altura=float(input("Ingrese su altura en cm : "))
resultado_imc=calcular_imc(peso,altura)
print(f"El IMC es {resultado_imc}")

"""///////////////////////////////////////////////////////////////////
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función."""
#Definición de funciones  (serán llamadas en cualquier parte del archivo de ser necesarias, pero se crean en cada ejercicio en particular)
def celsius_a_fahrenheit(celsius):
    return  (9/5)*celsius + 32
#Programa
celsius=float(input(" Ingrese la temperatura en grados Celsius: "))
grados_fahrenheit=celsius_a_fahrenheit(celsius)
print(f"la conversion de {celsius} grados celsius  a grados fahrenheit es {grados_fahrenheit}F ")


"""///////////////////////////////////////////////////////////////////
10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""
#Definición de funciones  (serán llamadas en cualquier parte del archivo de ser necesarias, pero se crean en cada ejercicio en particular)
def calcular_promedio(a, b, c):
    return (a+b+c)/3
    
#Programa
print("Ingrese tres números para calcular su promedio:")
a=float(input("ingrese el primer numero: "))
b=float(input("ingrese el segundo numero: "))
c=float(input("ingrese el tercer numero: "))
print(f"el promedio es {calcular_promedio(a,b,c)}")
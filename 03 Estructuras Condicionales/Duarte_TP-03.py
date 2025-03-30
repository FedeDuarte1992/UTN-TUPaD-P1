"""
1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”."""

edad=  int(input("ingrese su edad: "))
MAYOR_DE_EDAD= int(18)
if edad >= MAYOR_DE_EDAD :
    print("Es mayor de edad")
else :
    print ("No es mayor de edad")
print ("Gracias")

"""2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”."""

nota= int (input("Ingrese su nota: "))
APROBADO = int(6)
if nota >= APROBADO:
    print(f"Aprobaste con {nota}")
    print("Felicitaciones")
else:
    print(f"Desaprobaste con {nota}, no alcanza")
    print("Vuelve a intentarlo")
print("Gracias")

"""3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar."""

numero_par = int (input("Ingrese un numero par: "))
if numero_par % 2 == 0 : 
    print("Ha ingresado un número par")
else :
    print("Por favor, ingrese un número par")
print("Gracias")

"""4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
● Niño/a: menor de 12 años. 
● Adolescente: mayor o igual que 12 años y menor que 18 años. 
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
● Adulto/a: mayor o igual que 30 años."""

edad=int(input("Ingrese su edad: "))
if edad < 12 and edad > 0 :
    print(" Perteneces a la categoría Niño/a ")
elif edad >= 12 and edad < 18 : 
    print(" Pertenece a la categoría Adolescente ")
elif edad >= 18 and edad< 30 :
    print ("Pertenece a la categoría Adulto/a joven")
elif edad >= 30 :
    print ("Pertenece a la categoría Adulto/a mayor")
else : 
    print("ingrese un numero valido")

"""5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string. """

contrasenia = input("ingrese su contraseña de entre 8 y 14 caracteres: ")
if len (contrasenia) >= 8 and len (contrasenia) <= 14 :
    print("Ha ingresado una contraseña correcta123")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")    

"""6)escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla."""

from statistics import mode, median, mean 
import random
#crea una lista de numeros aleatorios
numeros_aleatorios=[random.randint(1,100) for i in range (20)]

#variables para las medias estadisticas 
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
#ahora se usa if para saber a cual corresponde 
if media > mediana and mediana > moda:
    sesgo = "Sesgo positivo "
elif media < mediana and mediana < moda:
    sesgo = "Sesgo negativo "
else:
    sesgo = "No hay sesgo evidente o distribución simétrica"

print(f"La lista generada es {numeros_aleatorios}, la media es {media}, la mediana es {mediana} y la moda es {moda}")

"""7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla."""

frase= input("ingrese una frase o palabra: ")
VOCALES= ('a','e','i','o','u','A','E','I','O','U')

if frase [-1] in VOCALES:
    frase += "!"
    print(f"{frase}")
else:
    print(f"{frase}")

"""8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas. """

nombre= input("ingrese su nombre: ")
opcion= int (input("elija una de las tres opciones : \n1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.\n2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro."))

if opcion == 1 :
    print (nombre.upper())
elif opcion ==2 :
    print (nombre.lower())
elif opcion==3:
    print (nombre.title())
else:
    print("ingrese una opcion valida")

"""9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)."""

magnitud = float(input("ingrese la magnitud "))

if magnitud < 3:
    print ("Es de magnitud Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4 :
    print ("Es de magnitud leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5 :
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6 :
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7 :
    print("Muy Fuerte (puede causar daños significativos)")
else :
    print("Extremo (puede causar graves daños a gran escala)")

"""10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano."""

hemisferio= input("Ingrese la primer letra de su hemisferio N/S: ")
mes=input("Ingrese en el mes: ")
dia=int(input("Ingrese el dia: "))
if hemisferio in ("N", "n"):
    if (mes in ("enero", "febrero")) or (mes == "diciembre" and dia >= 21) or (mes == "marzo" and dia <= 20):
        print("Se encuentra en el hemisferio norte y es invierno")
    elif (mes in ("abril", "mayo")) or (mes == "marzo" and dia >= 21) or (mes == "junio" and dia <= 20):
        print("Se encuentra en el hemisferio norte y es Primavera")
    elif (mes in ("julio", "agosto")) or (mes == "junio" and dia >= 21) or (mes == "septiembre" and dia <= 20):
        print("Se encuentra en el hemisferio norte y es Verano")
    elif (mes in ("octubre", "noviembre")) or (mes == "septiembre" and dia >= 21) or (mes == "diciembre" and dia <= 20):
        print("Se encuentra en el hemisferio norte y es Otoño")
    else:
        print("Fecha no válida para el hemisferio norte")
#se usa la misma estructura para el hemisferio sur
elif hemisferio in ("S", "s"):
    if (mes in ("julio", "agosto")) or (mes == "junio" and dia >= 21) or (mes == "septiembre" and dia <= 20):
        print("Se encuentra en el hemisferio Sur y es Invierno")
    elif (mes in ("octubre", "noviembre")) or (mes == "septiembre" and dia >= 21) or (mes == "diciembre" and dia <= 20):
        print("Se encuentra en el hemisferio sur y es Primavera")
    elif (mes in ("enero", "febrero")) or (mes == "diciembre" and dia >= 21) or (mes == "marzo" and dia <= 20):
        print("Se encuentra en el hemisferio sur y es Verano")
    elif (mes in ("abril", "mayo")) or (mes == "marzo" and dia >= 21) or (mes == "junio" and dia <= 20):
        print("Se encuentra en el hemisferio sur y es Otoño")
    else:
        print("Fecha no válida para el hemisferio sur")

else:
    print("Datos incorrectos: hemisferio no válido")
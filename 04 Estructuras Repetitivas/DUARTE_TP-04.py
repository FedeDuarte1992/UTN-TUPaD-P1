"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""

num=0 
for num in range(101 ) :
    print (num)
        
"""///////////////////////////////////////////////////////////////////
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
"""

numero_entero= int(input ("ingrese un numero entero: "))
if numero_entero == 0 :
    print("el numero tiene un solo dígito  ") 
else:
    contador = 0
    while numero_entero > 0 :
        numero_entero = numero_entero//10
        contador +=1
    print ("El numero tiene ", contador, "dígitos ")


"""///////////////////////////////////////////////////////////////////
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""

num_min=int(input("Ingrese el numero entero de Menor tamaño: "))
num_max=int(input("Ingrese el numero entero de Mayor tamaño: "))
num=0
contador=0
for num in range(num_min+1,num_max):
    contador += num
    print(contador)
"""///////////////////////////////////////////////////////////////////
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""

TERMINAR=0
contador=0
num= int(input("Ingrese un numero entero, para finalizar ingrese 0: "))
while num != TERMINAR:
    contador += num
    print(f"la suma es: {contador}")
    num=int(input("Ingrese otro numero: "))
print(f"Fin del programa, la suma total es {contador}")    

"""///////////////////////////////////////////////////////////////////
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

import random
num=int(input("ingrese un numero aleatorio entre 0 y 9:"))
numero_aleatorio=(random.randrange(0,10))
intentos = 1 
while num  != numero_aleatorio :
    intentos += 1   
    print(f"el numero ingresado {num} no es el ganador, siga intentando")
    num=int(input("ingrese otro numero: "))
print(f"el numero ingresado {num} es el ganador!!!!!! y lo lograste en {intentos} intentos")    

"""///////////////////////////////////////////////////////////////////
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""

num=0 
for num in range(100,0,-2 ) :
    print(f"{num}")
    

"""///////////////////////////////////////////////////////////////////
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""

num_ingresado= int(input("Ingrese un numero Entero mayor a 0 que sera el ultimo de la lista a sumar: "))
contador=0
for num in range(0,num_ingresado+1):
    contador += num 
    contador = num + contador
print(f"la suma comprendida entre 0 y {num_ingresado} es {contador}")

"""///////////////////////////////////////////////////////////////////
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

numero_par=0
numero_impar=0
numero_negativo=0
numero_positivo=0
TAMANIO_LISTA=5
cero=0
for num in range(TAMANIO_LISTA):
    num= int(input("Ingrese un numero: "))
    if num % 2 == 0 :
        numero_par +=1
    else:
        numero_impar +=1
    #para determinar si es par o impar, pero dentro del mismo bucle for se continua
    if num > 0:
        numero_positivo += 1
    elif num < 0:
        numero_negativo += 1
    else:
        cero += 1
if cero >= 1 :
    print("Se ingreso", cero, "cero que no se cuentan como validos")
    #ahora si se determina cual es positivo y negativo y se cuenta sin salir del bucle , se guarda en su var correspondiente 
print("Cantidad de números negativos:",numero_negativo)  
print("Cantidad de números positivos:",numero_positivo)         
print("Cantidad de números pares:",numero_par) 
print("Cantidad de números impares:",numero_impar) 


"""///////////////////////////////////////////////////////////////////
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor)."""

total=0
num=0
TAMANIO_LISTA=5
for num in range(TAMANIO_LISTA):
    num= int(input("Ingrese un numero entero: "))
    total += num 
media= total / TAMANIO_LISTA
print(f"la media de los {TAMANIO_LISTA} números es: {media}") 

"""///////////////////////////////////////////////////////////////////
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

num=int(input("ingrese un numero"))
invertido=0
digito=0
while num >0:
    digito= num% 10 #con esto se obtiene el ultimo digito
    invertido = invertido *10 + digito #con esto se van poniendo los dígitos en el orden inverso
    num= num //10 #se vuelve a eliminar el ultimo digito
print (f"El numero invertido es: {invertido}")
    


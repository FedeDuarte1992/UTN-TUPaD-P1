"""Ejercicio 1: Cálculo del área y el perímetro de un rectángulo 
Objetivo: Calcular el área y el perímetro a partir de medidas dadas por el 
usuario. 
Instrucciones: 
1. Pedir al usuario que ingrese el ancho y el alto de un rectángulo. 
2. Calcular el área usando la fórmula: ancho * alto. 
3. Calcular el perímetro con la fórmula: (ancho * 2) + (alto * 2). 
4. Mostrar ambos resultados en pantalla. 
Preguntas de reflexión: 
• ¿Qué sucede si se ingresan valores negativos? 
• ¿Podría adaptarse este cálculo a otras figuras geométricas?
lado=float(input("Ingrese el lado: "))
alto=float(input("Ingrese el alto: "))

area= (lado) * (alto)
perimetro = (lado * 2) + (alto * 2)
print(f"El area es: {area}")
print(f"El perimetro es {perimetro}")"""


""" Ejercicio 2: Conversión de grados Celsius a Fahrenheit 
Objetivo: Realizar la conversión de temperatura de Celsius a Fahrenheit. 
Instrucciones: 
1. Solicitar al usuario una temperatura en grados Celsius. 
2. Convertirla a Fahrenheit con la fórmula: F = (C * 9/5) + 32. 
3. Mostrar el resultado en pantalla. 
Preguntas de reflexión: 
• ¿Qué resultado se obtiene al ingresar 0°C? 
• ¿Cómo se adaptaría este ejercicio para convertir a Kelvin?
celsius= float(input("Ingrese la temperatura en grados Celsius: "))
Fahrenheit= (celsius*9/5) +32
kelvin= celsius + 273.15
print(f"los grados {celsius} comvertidos a Fahrenheit son {Fahrenheit} y a Kelvin : {kelvin}")
"""

"""Ejercicio 3: Uso de booleanos 
Objetivo: Manipular variables booleanas y aplicar operadores lógicos. 
Instrucciones: 
1. Declarar dos variables booleanas: a = True, b = False. 
2. Realizar e imprimir los resultados de las operaciones: 
        o a and b 
        o a or b 
        o not a, not b 
Preguntas de reflexión: 
• ¿Cuál es la utilidad de los operadores lógicos en programas más 
complejos? 
• ¿Qué representa cada operación? """
a= True
b= False

print (f"el resultado de a and  {a and b}")
print (f"el resultado de a or b {a or b}")
print (f"el resultado de not a  {not a} ")
print (f"el resultado de not b  {not b} ")
#1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
#Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500 
# ● Pera = 2300 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas ["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas ["Pera"] =2300
print("Ejercicio 1 ", precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330 
# ● Manzana = 1700 
# ● Melón = 2800 

#Aca opte por no volver a escribir el diccionario de nuevo ya que me parece innecesario 
precios_frutas ["Naranja"] = 1200
precios_frutas ["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas ["Melon"] =2800
print("Ejercicio 2 ", precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
frutas = list( precios_frutas.keys())
print("Ejercicio 3 ", frutas)

# 4) Crear una clase llamada Persona que contenga un método __init__ con los atributos nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad] años."
class Persona:
    def __init__(self,nombre,pais,edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad
    def saludar (self):
        print(f"Ejercicio: ¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")
# 5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.
# Ayuda: el módulo math puede ser de utilidad para usar la constante 𝜋.
import math

class Circulo:
    def __init__(self,radio):
        self.radio=radio
        
    def calcular_area(self):
        return math.pi * (self.radio ** 2) 
    
    def calcular_perimetro(self):
        return 2* math.pi * self.radio

ejemplo_de_circulo = Circulo(5) #aca se usa la clase con un valor de radio 5
print("Ejercicio 5: ")
print("Área:", ejemplo_de_circulo.calcular_area())       
print("Perímetro:", ejemplo_de_circulo.calcular_perimetro())  
        
#6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente balanceados usando una pila. 
# balanceado ("({[]})") -> True
# balanceado ("({[})") -> False
def balanceado(recorrido):
    pila = []
    parejas = {')': '(', '}': '{', ']': '['}
    for i in recorrido:
        if i in '({[':
            pila.append(i)
        elif i in ')}]':
            if not pila or pila.pop() != parejas[i]:
                return False
    return len(pila) == 0

print("Ejercicio 6 - Balanceado ({([])}):", balanceado("({([])})"))
print("Ejercicio 6 - Balanceado ({[}):", balanceado("({[})"))
# 7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:
# ● Agregar clientes (encolar).
# ● Atender clientes (desencolar).
# ● Mostrar el siguiente cliente en la fila.
from collections import deque
class Turno:
    def __init__(self):
        self.id = deque()
    def encolar (self,id):
        self.id.append(id)
    def desencolar(self):
        return self.id.popleft()if not self.esta_vacia()else "No hay mas turnos."
    def esta_vacia(self):
        return len(self.id) == 0 
    def siguiente(self):
        return self.id[0] if not self.esta_vacia() else "La cola está vacía"


turno = Turno()
print("Ejercicio 7: ")
turno.encolar("Turno 1")
turno.encolar("Turno 2")
turno.encolar("Turno 3")
turno.encolar("Turno 4")
print(turno.desencolar())
print("el siguiente en la lista es",turno.siguiente())

# 8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar los valores almacenados. 
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
    
    def recorrer(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

print("Ejercicio 8: ")
lista = ListaEnlazada()
lista.insertar_al_inicio(3)
lista.insertar_al_inicio(2)
lista.insertar_al_inicio(1)
lista.recorrer()
# 9) Dada una lista enlazada, implementa una función para invertirla. Ejemplo de entrada y salida:
# lista original 1--2--3-- none
# lista invertida 3--2--1--none
def invertir_lista(lista):
    anterior = None
    actual = lista.cabeza
    while actual:
        siguiente = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente
    lista.cabeza = anterior

# se toma la lista del ejercicio anterior 
print("Ejercicio 9: Lista original:")
lista.recorrer()

invertir_lista(lista)
print("Lista invertida:")
lista.recorrer()
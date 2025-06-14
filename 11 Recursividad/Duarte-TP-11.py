#-----------------------
print("-"*20,"Ejercicio 1","-"*20)
def factorial (numero):
    if numero == 0:
        return 1
    else :
        return numero * factorial(numero-1)
    
numero=int(input("Ingrese un numero entero: "))
print(f"El factorial entre 1 y ",numero," es ")
for i in range (1,numero+1):
    print(f"{i}  {factorial(i)}")

#-----------------------
print("-"*20,"Ejercicio 2","-"*20)
def fibo (pos):
        if pos == 0:
            return 0
        elif pos ==1:
            return 1
        else:
            return fibo (pos-1)+ fibo(pos-2)
print("Serie de fibonacci")
posicion_final=int(input("Ingrese la ultima posicion a calcular "))
for i in range(posicion_final + 1):
    print(f"{fibo(i)}")

#-----------------------
print("-"*20,"Ejercicio 3","-"*20)
def potencia(base,exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia (base, exponente -1)

base = int(input("ingrese la base: "))
exponente= int(input("ingrese el exponente: "))

resultado= potencia(base,exponente)
print(f"{base} elevado a  {exponente} = {resultado}")

#-----------------------
print("-"*20,"Ejercicio 4","-"*20)
def decimal_a_binario(decimal):
    if decimal == 0:
        return ''
    else:
        return decimal_a_binario (decimal//2) + str(decimal % 2)

decimal= int(input("ingrese un numero para ser covertido: "))
print("comversion de decimal a binario ")
binario= decimal_a_binario(decimal)
print(f"{binario}")

#-----------------------
print("-"*20,"Ejercicio 5","-"*20)
def es_palindromo(palabra):
    if len(palabra) <= 1 :#len es para acomodarver la cantida de letras
        return True
    elif palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])
palabra= input("ingrese la palabra para ver si es palindromo o no: ").lower()#transforma en minuscula
if es_palindromo(palabra):
    print(f"{palabra} es un palindromo")
else:
    print(f"{palabra} no es un palindromo")

#-----------------------
print("-"*20,"Ejercicio 6","-"*20)
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un numero entero: "))
print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}") 

#-----------------------
print("-"*20,"Ejercicio 7","-"*20)
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

n=int (input("ingrese un numero de bloques:  "))

n = int(input("Ingrese el número de bloques en el nivel más bajo de la pirámide: "))
print(f"La cantidad total de bloques necesarios es: {contar_bloques(n)}")






#-----------------------
print("-"*20,"Ejercicio 8","-"*20)

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    conteo = 1 if ultimo == digito else 0
    return conteo + contar_digito(numero // 10, digito)

numero = int(input("Ingrese un número entero : "))
digito = int(input("Ingrese el dígito  (0-9): "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")
def suma_recursiva_lista (lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0]+suma_recursiva_lista(lst[1:])
    
lista=[1,2,3,4,5,6]
print(f" el valor de la lista es {suma_recursiva_lista(lista)}")
#////////////////////////////////////////////////////////////////
def suma_recursiva_numero (n):
    if n == 0:
        return 0
    else:
        return n+ suma_recursiva_numero (n-1)
n=1
print(f"la suma de un numero es {suma_recursiva_numero(n)}")
#////////////////////////////////////////////////////////////////

def repeticion_de_diccionario (num,frase):
    if num >=1 :
        print(frase)
        repeticion_de_diccionario(num-1,frase)
#////////////////////////////////////////////////////////////////       
def fibo_recursividad (pos):
        if pos ==0:
            return 0
        elif pos ==1:
            return 1
        else:
           return fibo_recursividad (pos-1)+ fibo_recursividad(pos-2)
print(fibo_recursividad(9))

if __name__=="__Duarte-TP-11__":
    repeticion_de_diccionario(3,"hola mundo")
    
    

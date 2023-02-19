"""programa10
Nombre: Daniela M,V
Fecha: 9/02/23
Descripcion: realiza un programa que compare 2 numeros enteros e imprima el mayor de ellos , y si son iguales imprima none
"""
def mayor(numero1:int, numero2:int)->int|None
    result=None
    if numero1 > numero2:
        result = numero1
    elif numero2 > numero1:
        result = numero2
    return result

print(mayor(2,1)) #imprime el numero mayor  o menor o igual 
print(mayor(1,2)) #imprime el numero mayor  o menor o igual
print(mayor(2,2)) #imprime el numero mayor  o menor o igual
print(mayor(2,-1)) #imprime el numero mayor  o menor o igual
print(mayor(-1,2)) #imprime el numero mayor  o menor o igual
print(mayor(-1,-1)) #imprime el numero mayor  o menor o igual
print(mayor(-2,-1)) #imprime el numero mayor  o menor o igual
print(mayor(-1,-2)) #imprime el numero mayor  o menor o igual
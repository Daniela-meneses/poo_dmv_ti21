"""programa10
Nombre: Daniela M,V
Fecha: 9/02/23
Descripcion:
"""

def mayor(numero1 , numero2):
    result = None
    if numero1 > numero2:
        result = numero1
    elif numero2 > numero1:
        result = numero2 
    return result
    
print(mayor(2,1))
print(mayor(1,2))
print(mayor(2,2))
print(mayor(2,-1))
print(mayor(-1,2))
print(mayor(-1,-1))
print(mayor(-2,-1))
print(mayor(-1,-2))

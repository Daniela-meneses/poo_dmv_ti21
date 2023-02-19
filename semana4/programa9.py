"""programa9
Nombre: Daniela M,V
Fecha: 7/02/23
Descripcion: realiza un programa que compare 2 numeros enteros e imprima el mayor de ellos , y si son iguales imprima none
"""

n1 = int(input("numero1 :")) #variable tipo int o float
n2 = int(input("numero2 :")) #variable tipo int o float

#en esta operacion o ejecucion se da a conocer el numero mayor o menor entre los dos numeros
if n1 > n2 :
    print(n1) #imprime el numero mayor
if n2 > n1:
    print(n2) #imprime el numero mayor
if n1 == n2:
    print(None) #imprime None porque son iguales ambos numeros
#

#
if n2 > n1:
    print(n2) #imprime el numero mayor
if n1 > n2:
    print(n1) #imprime el numero mayor
else: 
    print(None) #imprime None porque son iguales ambos numeros
#

#
if n1 > n2:
    print(n1) #imprime el numero mayor
if n2 > n1:
    print(n2)  #imprime el numero mayor
else:
    print(None) #imprime None porque son iguales ambos numeros
#

#
if n1 == n2:
    print(None)  #imprime None porque son iguales ambos numeros
elif n1 > n2:
    print(n1) #imprime el numero mayor
elif n2 > n1:
    print(n2) #imprime el numero mayor
#

#
if n1 < n2:
    print(n2) #imprime el numero menor
if n2 < n1:
    print(n1) #imprime el numero menor
if n1 == n2:
    print(None) #imprime None porque son iguales ambos numeros
#

#
if n2 > n1:
    print(n2) #imprime el numero mayor
if n2 < n1:
    print(n1) #imprime el numero menor
else:
    print(None) #imprime None porque son iguales ambos numeros
#

#
if (n2<n1>n2):
    print(n1)
if (n1<n2>n1):
    print(n2)
else:
    print(None) #imprime None porque son iguales ambos numeros
#

#
if n1 <= n2:
    if n1 == n2:
         print(None) #imprime None porque son iguales ambos numeros
else:
    print(n2)
#

#
if n1 == n2: 
    print(None) #imprime None porque son iguales ambos numeros
if n1 < n2: 
    print(n2)  #imprime el numero menor
if n1 > n2: 
    print(n1)  #imprime el numero mayor
#

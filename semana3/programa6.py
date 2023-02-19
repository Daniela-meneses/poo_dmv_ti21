"""programa6
Nombre: Daniela M,V
Fecha: 30/01/23
Descripcion: Tarea de area y perimetro de un triangulo
"""

print("AREA Y PERIMETRO DE UN TRIANGULO") #imprime lo que se va a realizar 
print("ingrese la medida de la base de su triangulo") #imprime un mensaje para que el usuario pueda saber lo que le pide el programa
base = input("base :") # variable tipo int
print("ingrese la medida de la altura de su triangulo") #imprime un mensaje para que el usuario pueda saber lo que le pide el programa
altura = input("altura :") # variable tipo int 
print("ingrese la medida del lado1 de su triangulo") #imprime un mensaje para que el usuario pueda saber lo que le pide el programa
lado1 = input("lado1 :") # variable tipo int
print("ingrese la medida del lado2 de su triangulo") #imprime un mensaje para que el usuario pueda saber lo que le pide el programa
lado2 = input("lado2 :") # variable tipo int
print("el area de su triangulo es de :") #imprime un mensaje para que el usuario sepa de que es el resultado que se le mostro
areaa = float(altura) * float(base) / 2
print(areaa) #imprime el resultado de la operacion a realizar
print("el perimetro de su triangulo es de :")
perimetro = float(base) + float(lado1) + float(lado2) #imprime un mensaje para que el usuario sepa de que es el resultado que se le mostro
print(perimetro) #imprime el resultado de la operacion a realizar


 
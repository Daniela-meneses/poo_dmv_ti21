"""programa7
Nombre: Daniela M,V
Fecha: 31/01/23
Descripcion:area y perimetro de un circulo y cuadrado
"""
print("AREA Y PERIMETRO DE UN CIRCULO") #imprime lo que se va a realizar
print("ingrese la medida de el radio del circulo")  #imprime un mensaje para que el usuario pueda saber lo que le pide el programa
radio = input("radio :") #variable tipo int o float
print("el area de su circulo es de :") #imprime un mensaje para que el usuario sepa de que es el resultado que se le mostro
areaa = 3.14 * float(radio) ** 2 #operacion
print(areaa) #variable tipo int o float
print("el perimetro de su circulo es de :") #imprime un mensaje para que el usuario sepa de que es el resultado que se le mostro
perimetro = float(radio) * 3.14 * 2 #operacion
print(perimetro) #variable tipo int o float
print("AREA Y PERIMETRO DE UN CUADRADO") #imprime lo que se va a realizar
print("ingrese la medida del lado del cuadrado :")  #imprime un mensaje para que el usuario pueda saber lo que le pide el programa
lado = input("lado :") #variable tipo int o float
print("el area de su cuadrado es de :") #imprime un mensaje para que el usuario sepa de que es el resultado que se le mostro
area = float(lado) ** 2 #operacion
print(area) #variable tipo int o float
print("el perimetro de su cuadrado es de :") #imprime un mensaje para que el usuario sepa de que es el resultado que se le mostro
perimetro = float(lado) + float(lado) + float(lado) + float(lado) #operacion
print(perimetro) #variable tipo int o float

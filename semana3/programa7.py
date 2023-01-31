"""programa7
Nombre: Daniela M,V
Fecha: 31/01/23
Descripcion:area y perimetro de un circulo y cuadrado
"""
print("AREA Y PERIMETRO DE UN circulo")
print("ingrese la medida de el radio del circulo")
radio = input("radio :") #variable tipo int o float
print("el area de su circulo es de :")
areaa = float(radio) * 3.14 * float(radio)
print(areaa) #variable tipo int o float
print("el perimetro de su circulo es de :")
perimetro = float(radio) * 3.14 * 2
print(perimetro) #variable tipo int o float
print("ingrese la medida del lado del cuadrado :")
lado = input("lado :") #variable tipo int o float
print("el area de su cuadrado es de :")
area = float(lado) ** 2
print(area) #variable tipo int o float
print("el perimetro de su cuadrado es de :")
perimetro = float(lado) + float(lado) + float(lado) + float(lado)
print(perimetro) #variable tipo int o float
#Librerias 

from Colores.colors import red, yellow, green, bold, blue, reset, purple



#Codigo Principal

bold()
red()
a = int(input("Numero 1:"))

b = int(input("Numero 2:"))


blue()
print("Suma:", a + b)

reset()
bold()
print("Resta:", a - b)
green()

reset()
yellow()
print("Multiplicacion:", a * b)

reset()
bold()
purple()
print("Division:", a / b)

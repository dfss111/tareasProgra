#Trabajo 1
print("introduce un mes, pon toda la palabra en minuscula.")
condicion= input(" mes: ")

enero= 31
febrero=28
marzo= 30
abril= 31
mayo=30
junio=31
julio=30
agosto=31
septiembre=30
octubre=31
noviembre=30
diciembre=31

if condicion == "enero":
    print(enero)

elif condicion == "marzo":
    print(marzo)

elif condicion == "abril":
    print(abril)

elif condicion == "mayo":
    print(mayo)

elif condicion == "junio":
    print(junio)

elif condicion == "julio":
    print(julio)

elif condicion == "agosto":
    print(agosto)

elif condicion == "septiembre":
    print(septiembre)

elif condicion == "octubre":
    print(octubre)

elif condicion == "noviembre":
    print(noviembre)

elif condicion == "diciembre":
    print(diciembre)

#Trabajo 2

print("introduce un dia de la semana, pon toda la palabra en minuscula.")
condicion2= input(" dia de la semana: ")

lunes= 1
martes= 2
miercoles= 3
jueves= 4
viernes= 5
sabado= 6
domingo=7

if condicion2 == "lunes":
    print(lunes)

elif condicion2 == "martes":
    print(martes)

elif condicion2 == "miercoles":
    print(miercoles)

elif condicion2 == "jueves":
    print(jueves)

elif condicion2 == "viernes":
    print(viernes)

elif condicion2 == "sabado":
    print(sabado)

elif condicion2 == "domingo":
    print(domingo)


#Trabajo 3

variable1=int(input("escribe un año"))
if((variable1%4)== 0):
    print("el año que pusiste es bisiesto")

else:
    print("tu año no es bisiesto")

#Trabajo 4

var1=int(input("Escribe un año"))
if ((var1%4)== 0 ):
    print("Tu año es un año bisiesto")
else:
    print("Tu año no es un año bisiesto")

var2=int(input("Ingresa un numero"))
if ((var2>=0) and (var2<100) and ((var2%2)== 0)):
    print("Tu numero es positivo, menor a 100 y par")

elif ((var2>=0) and (var2<100) and ((var2%2)!= 0)):
    print("Tu numero es positivo, menor a 100 e impar")

elif ((var2>=0) and (var2>=100) and ((var2%2)== 0)):
    print("Tu numero es positivo, mayor o igual a 100 y par")

elif((var2>=0) and (var2>=100) and ((var2%2)!= 0)):
    print("Tu numero es positivo, mayor o igual a 100 e impar")

elif ((var2<0) and (var2<100) and ((var2%2)!= 0)):
    print("Tu numero es negativo, menor a 100 e impar")

else:
    print("Tu numero es negativo, menor a 100 y par")


# Ejercicio 5
list_1=["Do","Re","Mi","Fa","Sol","La","Si"]
list_1.insert(0,"Si")
list_1.insert(0,"Si")
list_1.insert(3,"Re")
list_1.insert(5,"Do")
list_1.insert(6,"Si")
list_1.insert(7,"La")
list_1.insert(8,"Sol")
list_1.remove("Mi")
list_1.remove("Fa")
list_1.insert(11,"Si")
list_1.insert(13,"La")
list_1.insert(14,"La")
print(list_1)


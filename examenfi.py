#Ejercicio 1
print("dar valor de corriente y voltaje: ")

c1= float ((input("corriente: ")))
r1= float((input("resistencia: ")))

voltaje=c1*r1

print(voltaje)

#Ejercicio 2

print("precios de vuelo del año pasado... ")
precio= float((input("precio:" )))

cost=8000

diferencia= (cost-precio)
print(diferencia)

porcentaje= float(precio*100)/cost
print("porcentaje de de la diferencia entre el vuelo del año pasado y el nuevo vuelo: ")
print(porcentaje)

#Ejercicio 3

print("escribe un numero para saber si es par o impar: ")
numero= int((input("numero: " )))

valor=(numero%2)
if(valor >0):
    print("impar")

else:
    print("par")


#Ejercicio 4 
 

#Ejercico 5
print("Da el valor de un lado y del apotema para iniciar...")

apotema= float(input("Apotema: "))
lado= float(input("Lado: "))

perimetro=(lado*6)


area=((perimetro*apotema)/2)

print=("su area es: ")
print=(area)

""" TEORIA: 
6.- .clear() y .copy()

7.- len()


8.- es un tipo de dato para poner texto


9.- float que sirve para contener los numeros decimales, e integros que son numeros no decimales


10.- una variable es un dato que el programa guarda 

11.- el and es tomar las vos variables que se te presenten, por ejemplo variable1 and variable2, se usaran ambas variables. 
    el or se refiere a o es una o es otra, por ejemplo num1 or num2, se usara solamente una de las dos. 
    finalmente not devuelve el valor contrario, por ejemplo le das true y te manda false."""

#Challenge1

print("a continuacion danos la base del triangulo...")

base= float(input("base: "))
altura= float(input("altura: "))

area=(base*altura)/2

print(area)













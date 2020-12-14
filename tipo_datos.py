# importo una libreria para usar el metodo write
# para imprimir en la misma linea
import os
import sys
import json

sys.stdout.write(' primera linea')
sys.stdout.write(' segunda linea')

# salto de linea
print('')

print('1')
print('2')
print('3')
# print ('4')
# print ('5')
print('6')
print('7')

print(2+2)

# concateno con el operador de mas o con la coma
# print ('2'+2)
print('2', 2)

# esto es un comentario

# esto es un
# comentario de
# bloque


print('variables: ')

n1 = 10
print(n1)  # 10
print('n1')  # n1

print('el valor de n1 es:', n1)

# str : string --> paso de un numero a un string para concatenar
# con el operador de +
print('el valor de n1 es: ' + str(n1))

n2 = 5

print('La suma de n1 y n2 es =', n1+n2)
print('La suma de n1 y n2 es = '+str(n1+n2))


# Variable entera:

edad = 21
print(edad)
print('La edad es : ', edad)
edad = edad+1
print('La edad es : ', edad)

# Variable flotante:

altura = 1.92
print('La altura es  : ', altura)
altura = altura+0.5
print('La altura es  : ', altura)


# Variable compleja:
# numero complejo
# parte real: 5 y parte imaginaria: 3

valor = 5+3j
print('El valor es : ', valor)


# Cadena de caracteres (puede estar encerrada entre simples o dobles comillas):

nombre = "Mario"
nombre2 = 'Maria'
print('el nombre es : ', nombre)
print('el nombre es : ', nombre2)

# Booleano:

encontrado = False
print(encontrado)
encontrado = True
print(encontrado)


# Ingreso por consola de Numeros
# valor = input ("Ingrese cantidad: ")
# print ("Usted ingreso: " +valor + "!")

# Ingreso por consola de Strings
#nombre = input ("¿Cual es tu nombre? ")
# print ("Hola, " + nombre+ " !")


# si nombro la variable nuevamente simplemente hago una nueva asignacion
# pero la asignacion debe ser en el mismo tipo de datos
edad = 25
print(edad)

# edad=juan
# print (edad)

lista = ["apple", "banana", "cherry"]

print(type(lista))

for elemento in lista:
    print(elemento)

dictionary = {"name": "John", "age": 31, "city": "New York"}

print(type(dictionary))

for elemento in dictionary:
    print(dictionary[elemento])

x = b"Hello"

print(type(x))
print(x)

x2 = bytearray(5)

#display x:
print(x2)

#display the data type of x:
print(type(x2)) 

print(os.getcwd())
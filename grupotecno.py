
""" Consigna:
Codificar en Python un programa que contenga las siguientes condiciones:
● El usuario debe ingresar 5 números enteros, los cuales serán almacenados en una
lista.
● Función Suma: recibe como parámetro la lista y devuelve la suma total de todos
sus elementos.
● Función Promedio: recibe como parámetro la lista y devuelve el promedio de sus
elementos.
● Función Máximo: recibe como parámetro la lista y devuelve el valor máximo de
todos los elementos que contiene.
● Función Mínimo: recibe como parámetro la lista y devuelve el valor mínimo de
todos los elementos que contiene."""
 
# Funciones
def suma(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma


def promedio(lista):
    promedio = suma(lista) / len(lista)
    return promedio


def maximo(lista):
    maximo = lista[0]
    for i in lista:
        if i > maximo:
            maximo = i
    return maximo


def minimo(lista):
    minimo = lista[0]
    for i in lista:
        if i < minimo:
            minimo = i
    return minimo


# Main
lista = []
for i in range(5):
    lista.append(int(input("Ingrese un numero: ")))
print("La suma de los numeros es: ", suma(lista))
print("El promedio de los numeros es: ", promedio(lista))
print("El numero maximo es: ", maximo(lista))
print("El numero minimo es: ", minimo(lista))

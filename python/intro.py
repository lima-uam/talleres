# Variables: guardan datos
nombre=""

print(f"Hola, {nombre}")
print()

# Tipos de datos simples
texto="Hola" # Cadena/texto (se puede usar "" o '')
entero=-3 # Enteros
decimal=1.32 # Decimales
booleano=True # Booleanos (True/False)

# Operaciones (entre variables o datos explícitos)
# Enteros y decimales: suma +, resta -, multiplicación *, división /
# Solo enteros: módulo/resto
resto=5%3 # Resto de la división
print(f"Resto de dividir 5 entre 3: {resto}")
print()

# Texto: unión de cadenas
texto="Hola "+"Pepe"
print(texto)
print()
# Cadenas con formato: f"" (permiten meter datos en cadenas)
pi=3.14
print(f"El valor de pi es {pi}")
print(f"También se pueden poner operaciones: 2+2={2+2}")
print()

# Booleanos: operaciones lógicas not, and, or
# Not: cambia True a False y viceversa
# a and b: True solo si a y b son True
# a or b: True si a o b (o ambas) son True
print(f"(not True)={not True}, (not False)={not False}")
print(f"(True and False)={True and False}")
print(f"(True or False)={True or False}")
print()

# Otros tipos de datos: colecciones
# Lista (ordenada, modificable)
lista = ["a", "b", "c"]
print(lista)
lista[0]="d" # Cambia el primer elemento
lista.remove("b") # Elimina "b"
lista.append("e") # Añade "e" al final
print(lista)
print(f"Longitud: {len(lista)}")
print()

# Tupla (ordenada, no modificable)
tupla = ("a", "b", "c")
print(tupla)
print(tupla[0])
# Si se intenta cambiar una tupla salta un error
print()

# Conjunto (sin orden ni repetición de elementos)
conjunto = {"a", "b", "c", "b"}
print(conjunto)
print()

# Diccionario (pares clave-valor)
diccionario = {"nombre": "Pepe", "apellido": "García"}
print(diccionario)
diccionario["teléfono"]=123456789
print(diccionario)
print()

# Expresiones que dan un valor True/False:
# Comparaciones de números: mayor que >, menor que <, 
# mayor o igual que >=, menor o igual que <=
print(f"3>4: {3>4}, 3<4: {3<4}")
print(f"3>3: {3>3}, 3>=3: {3>=3}")
# Comparaciones de variables en general: igual que ==, distinto !=
print(f"3==4: {3==4}, 'a'=='a': {'a'=='a'}")
print(f"3!=4: {3!=4}, 'a'!='a': {'a'!='a'}")
# No confundir a=3 con a==3:
#  a=3: da a la variable a el valor 3
#  a==3: comprueba si a vale 3
# Pertenencia a colecciones: in
print(f"1 in [1, 2, 3]: {1 in [1, 2, 3]}")
print(f"1 in [2, 3, 4]: {1 in [2, 3, 4]}")
print(f"1 not in [2, 3, 4]: {1 not in [2, 3, 4]}")
# Se pueden combinar entre sí y con los operadores lógicos
print(f"(3<4) and (1 in [1,2,3]):{(3<4) and (1 in [1,2,3])}")
print()

# Condicionales
# Indentación: espacio en blanco antes de cada línea.
# Python usa indentación para diferenciar los bloques de código
cond1=True
cond2=True
if cond1:
    print("cond1 es True")
    print("Continuamos el bloque con la misma indentación")
# los bloques elif y else son opcionales
elif cond2: # solo se comprueba si cond1 es False
    print("cond1 es False y cond2 es True")
# se pueden añadir todos los elif que se necesiten, 
# que se van comprobando en orden
else: # solo si ningun caso se cumple
    print("cond1 y cond2 son False")
print("Esto no es parte del condicional y se ejecuta siempre")

# Se pueden 'anidar', es decir, meter uno dentro de otro
if cond1:
    print("cond1 es True")
    if cond2:
        print("... y cond2 también")
print()

# Bucles: repiten instrucciones. Cada repetición se llama iteración.
# Se usan principalmente dos tipos
# while: mientras se cumple una condición
n = 0
while n < 5:
    print(n, end=" ")
    n = n+1 # Importante para evitar un bucle infinito
print()

# for: repiten el código para cada elemento de una colección
for palabra in ["casa", "coche", "perro"]:
    print(palabra, end=" ")
print()

# También funciona con cada letra de una cadena
for letra in "casa":
    print(letra, end=" ")
print()

# range: permite crear una lista de números rápidamente, útil para bucles:
comienzo=1
fin=10
paso=2
for i in range(comienzo, fin, paso): # de comienzo a fin-1, con paso=2
    print(i, end=" ")
print()
for i in range(comienzo, fin): # de comienzo a fin-1
    print(i, end=" ")
print()
for i in range(fin): # de 0 a fin-1
    print(i, end=" ")
print()
# Se puede usar para recorrer una lista teniendo un 'índice', i
print("lista:", lista)
for i in range(len(lista)):
    print(f"  lista[{i}]={lista[i]}")

# Interrumpir bucles
# break: se usa para salir del bucle inmediatamente
print("break: ", end="")
for palabra in ["España", "Andorra", "Francia"]:
    if palabra=="Andorra":
        break
    print(palabra, end=" ")
print()

# continue: se usa para saltar inmediatamente a la siguiente iteración
print("continue: ", end="")
for palabra in ["España", "Andorra", "Francia"]:
    if palabra=="Andorra":
        continue
    print(palabra, end=" ")
print()
# break y continue se deben usar dentro de un condicional (dentro del bucle)

print()
# Funciones: agrupan instrucciones bajo un nombre
# Parámetros/argumentos: datos que recibe la función entre paréntesis para usarlos
# Retorno: dato final que devuelve la función (opcional)
def funcion(argumento1, argumento2):
    return

# Función con retorno
def suma(a, b):
    return a+b
s=suma(1,2)
print(s)

# Función sin retorno
def escribe_lista(mi_lista):
    for i in range(len(mi_lista)):
        print(f"{i+1}. {mi_lista[i]}")
escribe_lista(lista)

# Python ofrece muchas funciones ya programadas, entre ellas 
# print(), len() y range() que ya hemos visto
# También hay funciones especiales que pertenecen a algunas variables,
# llamadas métodos. Se utilizan escribiendo variable.metodo(...), como
# lista.append(...) y lista.remove(...), que son métodos de las listas.

# Librerías: agrupan funciones para tareas más específicas.
import math # Importa la librería math entera
print(f"3^2={math.pow(3, 2)}") # Se accede a las funciones usando .

from random import randrange # Importa solo la función randrange
n_azar=randrange(20) # Se puede usar directamente la función
print(n_azar)

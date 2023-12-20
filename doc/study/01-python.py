# Mi primer comentario en python
from exports_py import pera #Descriptiva que es lo que yo quiero
"""
"""


print(pera.LO_QUE_VAMOS_A_EXPORT)

print(pera.my_func_module())
# Tipos de datos

"string"
'string'

20
10
30

True
False

None # nada null o undefined en javascript

# Lista
[1, 2, True, ""]

# Array 

[1, 2, 3, 4, 5]

# Inmutables

# Tuplas

(1, 2, 3)

# Objetos -> Diccionarios

{
    "key": "valor",
    "otro": 2,
    "boolean": True
}

# Nivel 

# Variable???

# snake case -> python === piton

# Python tipado debil
 
nombre_de_la_variable = "valor"

nombre_de_la_variable = 2

# console.log() -> print

print(nombre_de_la_variable)


# condicionales

edad = 18

# identancion
if edad >= 18:
   print("Es mayor")
else:
    print("Es menor")

if edad >= 19:
    print("WWW")
elif edad >= 18:
    if 2 == 2:
        print("222")
    print("www")
else:
    print("www")

list_de_variable = [1, 2, 3]

for i in list_de_variable:
    print(i)

def name_func():
    print("Identacion")

name_func()

try:
    print("valor a evular")
except:
    print("Error")
language = "python" #3

my_other_list = [17, 1.88, "Antu", "Code"] #4
my_list = [35, 12, 14, 34, 62, 17, 18, 30, 30] #4

my_tuple = (17, 1.88, "Antu", "Code", "Antu") #5
my_other_tuple = (35, 60, 30) #5

print("_____________________________________________________________________")
# Clase 3 Strings

"""
\t es tabulacion 
\n es cambio de linea
EL formteo mas correcto es print(f"MI {name} , {age} y {surname}")
Admite desempaquetado : a, b, c, d, e, f = lenguage
Slice: [1:2] Incluye el 1 pero no el 2 
       [1:]  Desde el 1 hacia delante
       [-2] lo mismo q solo pero los lugares se toman desde atrás
       [::-1] Imprimir en reversa
"""

print(language.capitalize()) # Pone mayúsculas
print(language.upper()) # TODO MAYUSCULAS
print(language.count("t")) # Cuenta la cant de caracteres especificados
print(language.isnumeric()) # Especifica si es un numero
print("2".isnumeric()) 
print(language.lower()) # todo minsculas
print(language.upper().isupper()) # Pregunta si se transformo con éxito
print(language.startswith("py")) # Pregunta si empieza por esos caracteres
print("Py" == "py") # No es lo mismo
print("_____________________________________________________________________")
# Clase 4 Lists
"""
Las listas son generalmente con [], admiten slice es decir [#], admiten desempaquetado y
operadores compatibles y admiten funciones como:
"""
print(my_other_list.index("Code"))

my_other_list.append("Anery") # Agrega a la lista
print(my_other_list)

my_other_list.insert(1, "Azul y Rojo") # Agrega en una posicion específica
print(my_other_list)

my_other_list[1] = "Rojo y Azul" # Se puede sustituir
print(my_other_list)

my_other_list.remove("Code") # Remueve el elemento
print(my_other_list)

my_list.remove(30) # SOLO EL PRIMER ELEMENTO (En este caso el primer 30)
print(my_list)

print(my_list.pop(2)) # Por defecto elimina el ultimo elemento
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)

del my_list[2] # A diferencia del pop este lo elimina para siempre
print(my_list)

my_new_list = my_list.copy()

my_list.clear() # Vacia la lista 
print(my_list)
print(my_new_list)

my_new_list.reverse() # Lo mismo que [::-1]
print(my_new_list)

my_new_list.sort() # Aleatorio pero puede incluir ordenes
print(my_new_list)

print(my_new_list[1:3]) # Slice
print("_____________________________________________________________________")
# Clase 5 Tuples
"""
Las listas son generalmente con (), admiten slice es decir [#],
operadores +, NO SON MODIFICABLES, SOLO PUEDES ELIMINARLAS 
TOTALMENTE O JUNTAR 2, y tiene 2 funciones:
"""

print(my_tuple.count("Antu")) 
print(my_tuple.index(1.88)) # Nos dice el índice del slice
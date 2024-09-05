### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 12, 14, 34, 62, 17, 18, 30, 30]
print(my_list)
print(len(my_list))

my_other_list = [17, 1.88, "Antu", "Code"]

print(type(my_list))
print(type(my_other_list)) # Las listas son otro tipo de dato que agrupa cualquier dato

# Slice
print(my_other_list[0]) 
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list[-4])
print(my_list.count(30))

age, height, name, surname = my_other_list # Desempaquetado
print(height)

age, surname, height, name = my_other_list[0], my_other_list[3], my_other_list[1], my_other_list[2]
print(height) #Aqui desempaquetamos pero indicando con slice (NO TENER MUCHO EN CUENTA)

# Funciones:

print(my_other_list + my_list)

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

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])

my_list = "Hola Python" # Con esto recordsmos que el typado de Python es dinámico
print(my_list)
print(type(my_list))


"""
Lesson 4 of mouredev
    AntuCode
"""
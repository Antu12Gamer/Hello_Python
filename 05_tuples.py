### Tuples ###

my_tuple = tuple()
my_other_tuple = (35, 60, 30)

my_tuple = (17, 1.88, "Antu", "Code", "Antu")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[-4]) IndexError

# Funciones
print(my_tuple.count("Antu")) 
print(my_tuple.index(1.88)) # Nos dice el índice del slice

#my_tuple[1] = 1.77 Aquí la diferencia con las listas ya que los tuples son inmutables 

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "AntuCode"
my_tuple.insert(1, "Rojo")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

del my_tuple # Solo se puede eliminar completo

"""
Lesson 5 of mouredev
    AntuCode
"""
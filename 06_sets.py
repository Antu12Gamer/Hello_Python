
### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Originalmente es un dict

my_other_set = {"Antu", "Code", 17}
print(type(my_other_set)) # Ahora sí es un set

print(len(my_other_set))

my_other_set.add("Anery")
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("Anery")
print(my_other_set) # Un set no admite repeticiones

print("Code" in my_other_set) # Verificando que esté en el set
print("Codi" in my_other_set)

my_other_set.remove("Code")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set)

my_set = {"Antu", "Code", 17}
my_list = list(my_set)
print(my_list)
print(my_list[1])

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set) #  Unir 2 sets pero no lo va a ordenar
print(my_new_set.union(my_new_set)) # No se van a unir 2 sets iguales

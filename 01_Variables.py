# Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

#He convertido mi variable int a str es decir mi número entero a una secuencia de texto
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True 
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

#Funciones del sistema
#1 Len= Contar la cantidad de carácteres
print(len(my_string_variable))
print(len(my_int_to_str_variable))
   #Adv SOLO OBJETO STR

# Variables en una sola línea ¡Cuidado con abusar de este truco!
name, surname, alias, age = "Antuán", "Lasuncet", "Antu", 17
print("Me llamo:", name, surname, ". Mi alias es:", alias, ". Y mi edad es:", age)   

#Inputs
name = input("Cuál es tu nombre?")
age = input("Tu edad?")

print(name)
print(age)
# Aquí se usó la misma variable pero se sobreescribió el valor

# Cambiamos su tipo
name = 17
age = "Antu"
print(name)
print(age)

# Forzamos el tipo?
address: str = "MI DIRECCION"
address = 34
print(type(address))

"""
Si ejecutas te daras cuenta que no podemos mantener el tipo de objeto
aunque lo especifiquemos, esto solo sirve para dar a entender que no 
queremos cambiar el tipo
"""

"""
Lesson 1 of mouredev
    AntuCode
"""


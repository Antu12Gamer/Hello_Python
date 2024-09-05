### Strings ###

my_string = "Mi String"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de línea"
print(my_new_line_string) 

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

my_escape_string = "\\tEste es un string \\n escapado" #Para que solo sea hablado poner otro \
print(my_escape_string)

#Formateo

name, surname, age = "Antu", "Code", 23

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) #Esta por rapidez
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) #Esta para el formateado
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #Super Rápido

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1] # Reversa
print(reversed_language)

# Funciones

print(language.capitalize()) # Pone mayúsculas
print(language.upper()) # TODO MAYUSCULAS
print(language.count("t")) # Cuenta la cant de caracteres especificados
print(language.isnumeric()) # Especifica si es un numero
print("2".isnumeric())
print(language.lower()) # todo minsculas
print(language.upper().isupper()) # Pregunta si se transformo con éxito
print(language.startswith("py")) # Pregunta si empieza por esos caracteres
print("Py" == "py") # No es lo mismo

"""
Lesson 3 of mouredev
    AntuCode
"""

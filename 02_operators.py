### Operadores Aritméticos ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3) # Es el resto de la division
print(10 // 3) # Aproxima el resultado a entero
print(2 ** 3) # Exponencial
print(2 ** 3 + 87 - 34 // 12)

print("Hola " + "Python " + "¿Qué tal?") # Hay operadores que funcionan con str
print("Hola " + str(5))
my_float = 2 ** 3 / 3 
print("Hola " * int(my_float)) # Esto es una prueba ya qe normalmente es el str * el num simple

### Operadores Comparativos ### (Dan una repuesta de True o False)
print("Comparativos 1") #NO ANALIZAR EN SU ESTUDIO ESTA LINEA#
print(3 > 4)
print(3 < 4) 
print(3 <= 4)
print(3 >= 4)
print(3 != 4)
print(3 == 4)

print("Comparativos 2") #NO ANALIZAR EN SU ESTUDIO ESTA LINEA#
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa") # Ordenación Alfabética por ASCII
print(len("aaaa") <= len("aaba")) # Por cant de caracteres
print("Hola" == "Python")
print("Hola" != "Python")

### Operadores Lógicos ###

#Formato booleano  (Puede ser varios términos a ordenar)
print("Lógico and") #NO ANALIZAR EN SU ESTUDIO ESTA LINEA#
#Con and lo proposicion va a ser 0,False hasta que todos sean 1,True
print(3 > 4 and "Hola" > "Python") #False  
print(3 > 4 and "Hola" < "Python") #False
print(3 < 4 and "Hola" > "Python") #False
print(3 < 4 and "Hola" < "Python") #True
print("Lógico or") #NO ANALIZAR EN SU ESTUDIO ESTA LINEA#
#Con or lo proposicion va a ser 1,True hasta que todos sean 0,False
print(3 > 4 or "Hola" > "Python") #False
print(3 > 4 or "Hola" < "Python") #True
print(3 < 4 or "Hola" > "Python") #True
print(3 < 4 or "Hola" < "Python") #True

"""
En definitiva se resume en:
And             Or
0 0 = 0     0 0 = 0
0 1 = 0     0 1 = 1
1 0 = 0     1 0 = 1
1 1 = 1     1 1 = 1
"""
print("Lógico not") #NO ANALIZAR EN SU ESTUDIO ESTA LINEA#
#Tenemos tambien a not el cual niega
print(not(3 > 4))

"""
Lesson 2 of mouredev
    AntuCode
"""
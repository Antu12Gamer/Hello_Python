name = input("Cómo te llamas? ")
print(f"Ohhh {name}, un bonito nombre la verdad\npero bueno este es un programa que te permitirá calcular palóndrimos")

palondrimo = input("Inserta tu palóndrimo: ").upper()
reversed_palondrimo = palondrimo[::-1]
ere = (palondrimo == reversed_palondrimo)
print(ere)


"""
Rezolvari exercitii practice Sesiune_1.1 - Fisiere Python, Variabile, Tipuri de date
"""

"""
EX1: 
a. Defineste o variabila de tip int, numita 'latime'.
b. Defineste o variabila de tip string, numita 'descriere'.
c. Defineste 2 variabile de tip float, numite 'pret' si 'discount'.
d. Defineste o variabila de tip bool, numita 'initializat' care are valoarea True.
e. Printeaza variabilele definite la punctele anterioare.
"""
print("rezolvare ex 1_________")
latime = 5
descriere = "patrat"
pret, discount = 1.5, 2.4
initializat = True
print(f"Latimea {descriere}ului este {latime}" 
      f" care este la un tarif {pret} cu un discount de {discount}"
      f" care e aplicat {initializat} de sarbatori")

"""
EX2: Folosind o singura linie de cod, defineste 2 variabile, de tip int, cu valoarea 10.
"""
print("rezolvare ex 2_________")
mate = romana =  10
print(f"Mate: {mate}"
      f" Romana: {romana}")

"""
EX7: 
a. Defineste o variabila de tip int. Afiseaz-o in consola.
b. Afiseaza in consola tipul variabilei definite la punctul a, folosind functia type().
c. Converteste variabila de tip int de la punctul a, la tipul float si salveaza rezultatul intr-o alta variabila.
d. Afiseaza in consola tipul variabilei generate la punctul c.
"""
print("rezolvare ex 7_________")
x = 50
print(type(x)) #pentru a afla tipul variabilei
print(f"punctul a \n {x}") #am afisat variabila in consola
y= float(x) # am convertit din int in float
print(f"punctul c \n {y}")
print(type(y))

"""
EX9: Citeste de la tastatura un nume de produs.
Salveaza rezultatul intr-o variabila.
Afiseaza un mesaj care sa contina variabila salvata.
"""
print("rezolvare ex 9_________")
nume_produs = input("Te rog introdu numele produsului:\n ")
print(f"Numele produsului este: {nume_produs}")

"""
EX10: Citeste de la tastatura un pret. Obliga utilizatorul sa introduca pretul ca si numar zecimal.
Salveaza rezultatul intr-o variabila.
Afiseaza un mesaj care sa contina variabila salvata.
"""
print("rezolvare ex 10_________")
pret = float(input("Introduceti pretul \n:"))
print(f"{nume_produs} costa {pret} lei ")
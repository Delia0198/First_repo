"""
EX1:
a. Defineste o lista cu 3 elemente.
b. Este lista o structura de date ordonata? De ce da/nu?
c. Acceseaza al doilea element din lista si afiseaza-l.
d. Afiseaza lungimea listei.
"""
# print("rezolvare ex1___________")
# lista_1 =  ["Portocale", "Mandarine", "Clementine"]
# print(lista_1)
# print(lista_1[1])
# print(len(lista_1))
# print("Lungimea listei de la ex 1 este len(lista_1)")


"""
EX5: Se da setul: my_set = {1, 2, 3, 4}.
a. Adauga nr 5 in set.
b. Adauga nr 6 in set.
c. Adauga nr 1 in set. Ce observi?
d. Sterge un element din set folosind metoda remove().
e. Sterge un element din set folosind metoda pop().
"""
# print("rezolvare ex5___________")
# my_set = {1, 2, 3, 4}
# my_set.add(5)
# my_set.add(6)
# my_set.add(1)
# my_set.remove(1)
# my_set.pop()
# my_set.pop()
# my_set.pop()
# print(my_set)


"""
EX6:
Se da urmatoarea structura de date:
locatie = (44.34, 12.456)
a. Verifica tipul structurii de date
b. Este aceasta structura de date ordonata?
c. Este aceasta structura de date mutabila?
d. Determina lungimea structurii de date.
e. Salveaza a doua valoare intr-o variabila.
Verifica daca aceasta este mai mare de 13, si afiseaza
un mesaj corespunzator.
"""

# print("rezolvare ex6___________")
# locatie = (44.34, 12.456)
# print(type(locatie))
# #b da
# #c nu pentru ca este un tuple
# print(len(locatie))
# a_doua_valoare = locatie[1] #fiinca incepe numerotarea de la 0
# if a_doua_valoare > 13:
#     print("Este mai mare")
# else:
#       print("Nu este mai mare")


"""
EX7: 
a. Defineste un dictionar, numit student1, cu urmatoarele chei:
nume, prenume, varsta, an_studiu, facultate, medie. 
Valorile le alegi tu.
b. Afiseaza lungimea dictionarului.
c. Printeaza prenumele studentului.
d. Adauga o noua pereche cheie-valoare, cu tara in care studiaza studentul.
e. Verifica daca dictionarul contine cheia oras.
"""
# print("rezolvare ex7___________")
# student1 = {
#     "nume": "Popescu",
#     "prenume": "Marius",
#     "varsta": 21,
#     "an_studiu": 2,
#     "facultate": "Matematica",
#     "medie": 9.75
# }
# print(len(student1))
# print(student1["prenume"])
# student1["tara"] = "Franta"
# if "oras" in student1:
#     print("Dictionarul contine cheia 'oras'")
# else:
#     print("Dictionarul nu contine cheia 'oras'")

"""
EX8:
a. Citeste de la tastatura urmatoarele date legate de o 
noua reteta: nume, ingrediente, timp prepapare.
b. Salveaza datele citite intr-un dictionar.
c. Actualizeaza numele retetei, scriind-ul cu litere mari.
"""
# #a
# nume_reteta = input("Te rog introdu nume reteta ")
# ingrediente_reteta = input("Te rog introdu ingrediente ")
# timp_prepapare = float(input("Te rog introdu timp prepapare "))
# #b
# dictionar = {
#        "nume": nume_reteta,
#        "ingrediente": ingrediente_reteta,
#        "timp": timp_prepapare
# }
# #c
# dictionar["nume"] = nume_reteta.upper()
# print(dictionar)


"""
EX9:
a. Se da un dictionar cu contacte din agenda telefonica:
contacte = {'Maria': '0722898956', 'Aurel': '0755342298'}
b. Aurel si-a schimbat numarul de telefon. Actualizeaza-l.
c. Ai obtinut numarul de telefon a lui Mihai. Adauga-l in contacte.
d. Maria a plecat in strainatate si nu mai are numar de telefon. Sterge-l.
e. Verifica daca ai numarul Mihaelei si afiseaza un mesaj corespunzator.
"""
#a
contacte = {'Maria': '0722898956', 'Aurel': '0755342298'}
#b
contacte['Aurel'] ='0785412696' #modificam date Aurel in dictionar
print("Noul contact pentru Aurel", contacte)
#c


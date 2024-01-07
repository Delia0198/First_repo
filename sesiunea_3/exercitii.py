"""
Solutii exercitii sesiunea 3- Recapitulare sesiunea 1 si sesiunea 2
"""
"""
7. Citește de la tastatură:
lungimea;
lățimea.
   Afișează: 'Aria dreptunghiului este x'.
"""
# print("rezolvare ex 7_________")
# lungime = int(input("Introdu lungimea dreptunghiului:"))
# latime = int(input("Introdu latimea dreptunghiului: "))
# aria = lungime * latime
# print(f"Aria dreptunghiului este egala cu {aria}")

"""
8.
X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare
"""
# print("rezolvare ex 8_________")
# x = int(input("Introduceti lungimea l1:"))
# y = int(input("Introduceti lungimea l2:"))
# z = int(input("Introduceti lungimea l3:"))
# if x == y == z:
#     print("Triunghiul este echilateral")
# elif x == y or x == z or y == z:
#     print("Triunghiul este isoscel")
# else:
#     print("Triunghiul este oarecare")

"""8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
afișează de câte ori apare cuvântul 'the';
"""
# phrase = "Coral is either the stupidest animal or the smartest rock" # am stocat informatia stringului in memoria variabilei phrase
# print(phrase.count(" the ")) # cauta de cate ori apare cuvantul in string
# numar = phrase.count( " the ") # am introdus valoarea intr-o variabila
# print(f"In cadrul stringului dat cuvantul 'the' apare de {numar} ori") #am afisat pe ecran

"""
12.Verifică dacă x are exact 6 cifre.
"""
# x = int(input("Va rugam introduceti o valoare")) #am introdus de la tastatura o variabila
# if len(str(x)) == 6: #am convertit in string si am verificat daca lungimea stringului este 6
#     print("Egal cu 6") # am printat mesaj pozitiv
# else: #daca lungimea nu este 6
#     print("Nu este egal cu 6") #am printat mesaj negativ
"""
15. 
X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.
"""

# x = int(input("Introduceti primul unghi:"))
# y = int(input("Introduceti al doilea unghi:"))
# z = int(input("Introduceti al treilea unghi:"))
# suma_unghiurilor = x + y + z
# if suma_unghiurilor == 180 and x > 0 and y > 0 and z > 0:
#   print("Triunghiul este valid")
# else:
#     print("Triunghiul nu este valid")

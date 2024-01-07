"""
21. Având stringul '0123456789'
Afișează doar numerele pare
Afișează doar numerele impare
(hint: folosește slicing, controlează din pas)

"""
sir =  '0123456789' #am declarat si initializat un string
numere_pare = sir[::2] #pentru numerele pare am inceput de la primul caracter, adica  pozitia 0, pana la ultimul caracter, pozitia 9, unde am folosit un pas de 2 astfel incat sa selecteze doar numerele pare
print("Numere pare:", numere_pare) #am printat numerele pare
numere_impare = sir[1::2] # pentru numrele impare am inceput de la pozitia 1 si am mers pana la pozitia 9, cu pas de 2 pentru a selecta doar numerele impare
print("Numere impare:", numere_impare) #am printat numerele impare
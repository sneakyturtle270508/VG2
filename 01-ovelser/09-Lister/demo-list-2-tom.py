# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-10-14 08:03:35
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-10-14 11:08:10
# # BEHANDLING AV LISTER(ARRAYS) i PYTHON

# # Opprett en liste med elementer
# liste_a = ["Kari","Petter","Thore","Per"]

# # Skriv ut en liste
# print(liste_a)


# # Kontroller at det er en liste
# print(type(liste_a))

# # Hvor mange elementer inneholder en liste
# print(len(liste_a))


# # Opprett en tom liste
# liste_b = []


# # Legg til et element i en liste
# liste_b.append("blå")
# print(liste_b)
# liste_b.append("rød")
# print(liste_b)


# # Tillatt med duplikate verdier i liste
# liste_a.append("Petter")
# print(liste_a)

# # les et element i en liste. Fra starten og fra enden. 
# print(liste_a[0])
# print(liste_a[-1]) # Siste element i lista

# # Endre et element i en liste
# liste_a[2] = "Kåre" 
# print(liste_a)

# # Sett inn et element i en liste
# liste_a.insert(1, "Henrik")
# print(liste_a)

# # Slett element i liste på innhold
# liste_a.remove("Petter")
# print(liste_a)

# # Slett element i liste på index-nummer
# liste_a.pop(2)
# print(liste_a)

# # En tekststreng (string) er en liste. OBS! Du kan ikke kjøre append på en string.
best = [2,4,6,5]
uke = ["man", "tir", "ons", ]
# print(navn[2])
maxBest = 0


# Løkker og lister
for i in range(len(best)):
    for tall in best:
        maxBest += best[i]
    
    print(maxBest)
       
uke= ["man", "tir", "ons", "tors"]
min_liste = [1, 5, 10, 2]
total = 0
index = None

for i in range(len(min_liste)):
    total += min_liste[i]
    

print("Total:", total)
print("Indeksen til tallet 5 er:", index)
print(uke[i])

# sum
bestilling = [1, 5, 10, 2]
total = 0

for tall in bestilling:
    total += tall

print(total)

# for i in range(1,len(liste_a),2):
#     print(liste_a[i])     




liste = [4, 7, 2, 9, 1]
maks = liste[0]  # start med første tall

for tall in liste:
    if tall > maks:
        maks = tall

print("Største tall:", maks)
storeDager = []
gjennomsnitt=3
for tall in liste:
    if gjennomsnitt < tall:
        storeDager.append(tall)
        
print(storeDager)
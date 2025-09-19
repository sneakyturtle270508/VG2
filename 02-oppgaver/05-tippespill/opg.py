# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-09-09 10:58:29
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-12 13:43:06
# importer random


import random


# lag variabelen talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet
# sett den til et tilfeldig tall mellom 1 og 10

talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet = random.randint(1, 10)

# lag variabelen brukerForsok
# sett den til 0
brukerForsok = 0




# while-løkke
while True:
    
#     be brukeren skrive inn et tall
    inputtSomBrukerGirTerminalen = input("Hvilke tall gjetter du: ")
    
   

#     hvis input ikke består av bare tall
    if not inputtSomBrukerGirTerminalen.isdigit(): # Lærer: Flott at du sjekker at brukerens input er heltall. 
#         skriv "du må skrive inn et heltall"
        print("Du må skrive inn et heltall.")
#         fortsett til neste runde
        continue
    
   

#     gjør om input til heltall
    inputtSomBrukerGirTerminalen = int(inputtSomBrukerGirTerminalen)
#     øk antall forsøk med 1
    brukerForsok += 1
    
   

#    hvis gjettet tall er større enn tallet som skal gjettes
    if inputtSomBrukerGirTerminalen > talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet:
#         skriv "tallet er lavere"
        print("Tallet er lavere")
#     eller hvis gjettet tall er mindre enn tallet som skal gjettes
    elif inputtSomBrukerGirTerminalen < talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet:
#         skriv "tallet er høyere"
        print("Tallet er høyere")
#     eller
    else:
#         skriv "du gjettet riktig"
        print("Du gjettet riktig!")
#         skriv antall forsøk
        print(f"Antall forsøk: {brukerForsok}")
#         break
        break


# Lærer: Du kommer i mål med denne oppgaven, men som jeg kommenterte tidligere er jeg ikke så
#        tilhenger av å bruke "True" i while-betingelsen. Grunnen er at du lager en evig løkke og så må
#        en lete nedover i koden for å finne "break". Det kan da være vanskelige å finne ut hva som faktisk
#        stopper løkka. Fint at du har laget en alternativ løsning.
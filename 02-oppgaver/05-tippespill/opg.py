# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-09-09 10:58:29
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-09 21:23:36
# importer random
import random

# lag variabelen talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet 
# gi variabelen talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet et randomt tall mellom 1 og 10
talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet = random.randint(1, 10)

#     lag variabelen inputtSomBrukerGirTerminalen
#     gi variabelen inputtSomBrukerGirTerminalen verdi int inputt
try: 
    inputtSomBrukerGirTerminalen = int(input("Hvilke tall gjetter du: "))
#     sjekk om bruker skrev in et tall
#     gir all verdierror print som sier at bruker må skrive in et tall

except ValueError:
    print("Du må skrive inn et heltall.\nKjør på nytt for å prøve igjen...")
    exit()

# så lenge inputtSomBrukerGirTerminalen ikke er lik talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet
while inputtSomBrukerGirTerminalen != talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet:
    
    
    
    
    #     hvis inputtSomBrukerGirTerminalen er større en talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet
    if inputtSomBrukerGirTerminalen > talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet:
    #         print tallet er lavere
        print("tallet er lavere")
    #     eller inputtSomBrukerGirTerminalen er mindre en talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet
    elif inputtSomBrukerGirTerminalen < talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet:
    # print tallet er høyere
        print("Tallet er høyere")
    
    # spør bruker hvilke tall den jetter
    inputtSomBrukerGirTerminalen = int(input("Hvilke tall gjetter du: "))
# print du gjettet rinktig tall
print("du gjettet riktig")
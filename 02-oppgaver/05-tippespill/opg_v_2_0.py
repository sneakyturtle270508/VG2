# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-09-09 10:58:29
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-19 13:24:13
# importer random
import random

# lag variabelen heltalletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet 
# gi variabelen heltalletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet et randomt tall
heltalletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet = random.randint(1, 10)

#     lag variabelen inputtSomBrukerGirTerminalen
#     gi variabelen inputtSomBrukerGirTerminalen verdi int inputt
inputtSomBrukerGirTerminalen = int(input("Hvilke tall gjetter du: "))

    
# så lenge inputtSomBrukerGirTerminalen ikke er lik heltalletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet
while inputtSomBrukerGirTerminalen != heltalletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet:
    
        

# spør bruker hvilke tall den jetter
    
    #     hvis inputtSomBrukerGirTerminalen er større en heltalletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet
    if inputtSomBrukerGirTerminalen > heltalletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet:
    #         print tallet er lavere
        print("tallet er lavere")
    #     eller inputtSomBrukerGirTerminalen er mindre en heltalletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet
    elif inputtSomBrukerGirTerminalen < heltalletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet: # Lærer: Her kunne du bare brukt "else".
    # print tallet er høyere
        print("Tallet er høyere")
    
    inputtSomBrukerGirTerminalen = int(input("Hvilke tall gjetter du: "))
# print du gjettet rinktig tall
print("du gjettet riktig")

# Lærer: Fin alternativ løsning som jeg synes blir enklere å lese. Bra! :-)


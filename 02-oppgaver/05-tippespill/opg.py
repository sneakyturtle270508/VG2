# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-09-09 10:58:29
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-09 11:22:50
# importer random
import random

# lag variabelen talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet 
# gi variabelen talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet et randomt tall
talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet = random.randint(1, 10)

#     lag variabelen inputtSomBrukerGirTerminalen
#     gi variabelen inputtSomBrukerGirTerminalen verdi int inputt
inputtSomBrukerGirTerminalen = int(input("Hvilke tall gjetter du: "))

# så lenge inputtSomBrukerGirTerminalen ikke er lik talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet
while inputtSomBrukerGirTerminalen != talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet:
    
    
    
# spør bruker hvilke tall den jetter
    
    #     hvis inputtSomBrukerGirTerminalen er større en talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet
    if inputtSomBrukerGirTerminalen > talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet:
    #         print tallet er lavere
        print("tallet er lavere")
    #     eller inputtSomBrukerGirTerminalen er mindre en talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet
    elif inputtSomBrukerGirTerminalen < talletSomSkalBliGjettetAvBrukerenSomBrukerProgrammet:
    # print tallet er høyere
        print("Tallet er høyere")
    
    inputtSomBrukerGirTerminalen = int(input("Hvilke tall gjetter du: "))
# print du gjettet rinktig tall
print("du gjettet riktig")
# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-08-23 18:00:18
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-08-23 18:13:10

alder = int(input("skriv in alderen din: "))# vi lager en variabel med tallet 19

if alder >= 18:         # sjekker om alder er større enn eller lik 18
    print("du er myndig")   # hvis det stemmer -> skriv ut denne teksten
else:                   # ellers, hvis det IKKE stemmer
    print("ikke myndig")    # da skrives denne teksten


for i in range(alder + 2):
    print ("hei", i)
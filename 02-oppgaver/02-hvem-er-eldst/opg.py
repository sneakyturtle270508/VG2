# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-08-29 10:44:00
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-03 20:39:37

# lag variabelen henrik
# gi variabelen henrik verdi input fra bruker /kun tall
    # skriv til brukeren: skriv inn alderen til henrik:
henrik = int(input("skriv inn alderen til Henrik: "))

# lag variabelen kari
# gi variabelen kari verdi input fra bruker /kun tall
     # skriv til brukeren: skriv inn alderen til kari:
kari = int(input("skriv inn alderen til Kari: "))

# hvis alder er lik
if henrik == kari:
    # skriv de er like gamle
    print("de er like gamle")
# eller hvis alderen til henrik er eldst
elif henrik > kari:
    # skriv henrik er eldst
    print("henrik er eldst")
# eller
else:
    # skriv kari er eldst
    print("kari er eldst")


# Lærer: Flott løsning, William! 
#        En liten detalj: Start alle setninger du skriver til skjem med stor bokstav :-)    
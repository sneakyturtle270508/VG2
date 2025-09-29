# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-09-23 10:46:06
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-26 13:17:16


# arket:
#      x|                  |x
# -------------------------------
#       |                  |
#       |                  |
#       |                  |
# -------------------------------
#      x|                  |x


# --------------opg1------------------------

# lag funksjonen box og gi parameteret h
def box(h):
    # lag variabelen b og bruk regnestyke 21.0 - (h* 2.0)
    # dette gjør at man finner bredde med bare høyde
    # grunnen til h * 2 er at man har 2 x er på arket som skal fjernes.
    b = 21.0 - (h * 2.0)

    # lag variabelen l og bruk regnestykket 29.7 - (h * 2.0)
    # dette gjør at man finner lengden med bare høyde
    # grunnen til h * 2 er at man har 2 x-er på arket som skal fjernes.
    l = 29.7 - (h * 2.0)

    #  lag volum formelen
    v = l * b * h
    return(v)

# ta imot brukerens box høde
# v = int(input("skriv inn høyden: "))
# print(box(v))
# --------------slutt / opg1--------------------

# --------------start / opg2--------------------
# legg til stegene den skal ta hver gang den sjekker. slik som i en løkke.
steg = 0.1
#lag variabelen storstVerdi og giv verdi 0
storstVerdi = 0

# lag en while løkke som sjekker om storstverdi er større eller mindre en storstVerdi  + steg
while box(storstVerdi) < box(storstVerdi + steg):
    # hvis den er større legg til verdien til steg i storstVerdi
    storstVerdi += steg

# print ut hva som er det mest opptimale tallet
print(f"her er det mest optimale {storstVerdi}")

# --------------slutt / opg2--------------------


# Lærer: Veldig bra og godt dokumentert, William. Her har du også fått med hva som må skje 
#        i while-løkka

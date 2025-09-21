# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-09-21 13:23:55
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-21 14:23:08
import os

os.system("cls")

print("""Velg hvilken kalkulator du vil ha: 
1. binær til hexadesimal
2. hexadesimal til binær
3. heltall til binær
4. binær til heltall
5. heltall til hexadesimal
6. hexadesimal til heltall""")

userInput = int(input("Velg her: "))

if userInput < 1 or userInput > 6:
    print("Det er bare 6 ting på denne listen")
elif userInput == 1:
    biner = input("Skriv inn binærtallet du skal oversette: ")
    print(f"Hex: {hex(int(biner, 2))[2:]}")
elif userInput == 2:
    heks = input("Skriv inn hexadesimaltallet du skal oversette: ")
    print(f"Binær: {bin(int(heks, 16))[2:]}")
elif userInput == 3:
    heltall = int(input("Skriv inn heltallet du skal oversette: "))
    print(f"Binær: {bin(heltall)[2:]}")
elif userInput == 4:
    biner = input("Skriv inn binærtallet du skal oversette: ")
    print(f"Heltall: {int(biner, 2)}")
elif userInput == 5:
    heltall = int(input("Skriv inn heltallet du skal oversette: "))
    print(f"Hex: {hex(heltall)[2:]}")
else:
    heks = input("Skriv inn hexadesimaltallet du skal oversette: ")
    print(f"Heltall: {int(heks, 16)}")

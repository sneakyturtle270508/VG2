# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-08-26 13:23:32
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-08-28 22:13:44


# importer random bibilioteket
import random
# importer time biblioteket
import time

# lag variabelen poeng 
# sett verdien til poeng til 0
poeng = 0

# lag en løkke som kjører 10 ganger
for i in range(10):
    
    # lag variabelen tall1
    # gi tall1 verdien et random tall 
    tall1 = random.randint(1,10)
    # lag variabelen tall2
    # gi tall2 verdien et random tall  
    tall2 = random.randint(1,10) 

    # lag variabelen sum for å multiplisere tall1 og tall2
    sum = tall1 * tall2
    
    
    print("___________________________________________________")
    # skriv spørsmål nr. verdien til i inni løkken
    # ny linje
    # skriv til brukeren hva de to tallene er 
    print(f"\nspørsmål nr{i+1}:\noppgaven:\n     {tall1} * {tall2}")

    # lag en variabel som heter svar
    # gi variabelen svar verdien at brukeren får skrive inn
    svar = int(input("skriv svaret her: "))
    
    # programmet venter 1 sekund
    # skriv sjekker fasit...
    # programmet venter 1 sekunder
    time.sleep(1)
    print("sjekker fasit...")
    time.sleep(1)
    
    # hvis svaret var riktig
        # legg til 1 poeng i variabelen poeng
        # skriv du svarte riktig
        # skriv ut verdien til variabelen poeng
    if svar == sum:
        poeng +=1
        print("\ndu svarte riktig")
        print(f"Antall poeng: {poeng}")
        
    # hvis svaret var feil
        # skriv du svarte feil
        # skriv ut verdien til variabelen poeng
    else:
        print("Feil svar!")
        print(f"Antall poeng: {poeng}")
        
# hvis variabelen poeng har verdi 10
    # skriv Supert! Du er god!
if poeng == 10:
    print("___________________________________________________")
    print("\nSupert! du er god!")
    print("___________________________________________________")
# eller hvis variabelen poeng har verdi 9
    # dette var bra!
elif poeng == 9:
    print("___________________________________________________")
    print("\nDette var bra")
    print("___________________________________________________")
# eller hvis variabelen poeng har verdi 8
    # skriv bra, men du må øve mer!
elif poeng == 8:
    print("___________________________________________________")
    print("\nBra, men du må øve mer")
    print("___________________________________________________")
# eller
    # du må øve mere!
else:
    print("___________________________________________________")
    print("\ndu må øve mer")
    print("___________________________________________________")



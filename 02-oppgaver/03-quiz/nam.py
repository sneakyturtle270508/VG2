# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-09-03 13:35:27
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-03 19:32:53
import time

poengTeller = 0
poengTellerMotsatt = 0

print("📝 Velkommen til quizen! Du trenger bare å svare med ett ord.\n")

# Funksjon for ASCII-ramme rundt teksten
def ascii_box(msg):
    linje = "┌" + "─" * (len(msg)+2) + "┐"
    sluttramme = "└" + "─" * (len(msg)+2) + "┘"
    print(linje)
    print(f"│ {msg} │")
    print(sluttramme)
    print("\n")
    time.sleep(0.5)

# -------------------
# Spørsmål 1
svar1 = input("1. hva er hovedstaden i norge: ").lower()
if svar1 == "oslo":
    poengTeller += 1
    ascii_box("Riktig")
else:
    poengTellerMotsatt += 1
    ascii_box("Feil!")

# Spørsmål 2
svar2 = input("2. hvilke programmeringspråk bruker KI: ").lower()
if svar2 == "python":
    poengTeller += 1
    ascii_box("Riktig!")
else:
    poengTellerMotsatt += 1
    ascii_box("Feil!")

# Spørsmål 3
svar3 = input("3. hva er filformatet til en tekstfil: ").lower()
if svar3 == ".txt":
    poengTeller += 1
    ascii_box("Riktig!")
else:
    poengTellerMotsatt += 1
    ascii_box("Feil!")

# Spørsmål 4
svar4 = input("4. hva heter jeg som lagde dette: ").lower()
if svar4 == "william":
    poengTeller += 1
    ascii_box("Riktig!")
else:
    poengTellerMotsatt += 1
    ascii_box("Feil!")

# Spørsmål 5
svar5 = input("5. hva er min alder: ").lower()
if svar5 == "17":
    poengTeller += 1
    ascii_box("Riktig!")
else:
    poengTellerMotsatt += 1
    ascii_box("Feil!")

# Spørsmål 6
svar6 = input("6. puster du: ").lower()
if svar6 == "ja":
    poengTeller += 1
    ascii_box("Riktig!")
else:
    poengTellerMotsatt += 1
    ascii_box("Feil!")

# Spørsmål 7
svar7 = input("7. bruker du vs code nå: ").lower()
if svar7 == "ja":
    poengTeller += 1
    ascii_box("Riktig!")
else:
    poengTellerMotsatt += 1
    ascii_box("Feil!")

# Spørsmål 8
svar8 = input("8. liker jeg(William) noe annet en oneplus som tlf: ").lower()
if svar8 == "ja":
    poengTeller += 1
    ascii_box("Riktig!")
else:
    poengTellerMotsatt += 1
    ascii_box("Feil!")

# Spørsmål 9
svar9 = input("9. bruker du windows nå: ").lower()
if svar9 == "ja":
    poengTeller += 1
    ascii_box("🎉Riktig!🎉")
else:
    poengTellerMotsatt += 1
    ascii_box("Feil!")

# Spørsmål 10
svar10 = input("10. bruker du en skjerm for å se på dette: ").lower()
if svar10 == "ja":
    poengTeller += 1
    ascii_box("Riktig!")
else:
    poengTellerMotsatt += 1
    ascii_box("Feil!")

# -------------------
# Resultat med ASCII-stjerner og kryss
ascii_box(f"Du fikk {poengTeller} riktige! {'⭐'*poengTeller}")
ascii_box(f"Du fikk {poengTellerMotsatt} feil. {'❌'*poengTellerMotsatt}")

print("Start programmet på nytt for å prøve igjen...")

# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-10-17 10:55:43

ukedager = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]
bestillinger = [43, 56, 38, 70, 65, 44, 52]
lengde = 7
def totalBestillinger(l):
  
  
    total = 0
    for nummer in l:
        total += nummer
        

    return total

total = totalBestillinger(bestillinger)

def maxOgDag(l):
    index = None
    maks = 0

    for teller in l:            # Lærer: Hadde du trengt to for-løkker i denne funksjonen?
        if teller > maks:
            maks = teller

    for i in range(lengde):
        if l[i] == maks:
            index = i
        
    # Lærer: Dersom du fil bruke listen "ukedager" inne i funksjonen, bør du ta denne listen inn som et parameter.
    #        Nå er funksjonen din avhengig av at det finnes en global liste utenfor funksjonen som heter "ukedager".  
    print(f"Dagen med flest bestillinger var {ukedager[index]} med {bestillinger[index]} bestillinger")
    # Lærer: Foreta gjerne printing til skjerm utenfor funksjonen.
    return (maks, index)



#   lag funksjonen gjennomsnitt
def overGjennomsnitt(t, l):  # Lærer: Denne funksjonen er avhengig av at noen har kjørt funksjonen "totalBestillinger" først. Pass på
                             #        at hver funksjon kan brukes uten at de er avhenging av andre egendefinerte funksjonen. Først da 
                             #        kan de regnes som selvstendige.
    gjennomsnitt = t / lengde
   
#         gi verdi sum(bestillinger) / len(bestillinger)
    dager = []
   
    for i in range(len(ukedager)):
        if l[i] > gjennomsnitt:
            dager.append(ukedager[i])
    
    print(f"dagene med mere en gjennomsnitt i bestillinge er {dager}")
    return dager




print("bestillinger gjennom uka:")
resultatUke = ' | '.join(ukedager)
result = '      | '.join(map(str, bestillinger))
print(resultatUke)
print(result)

print(f"den totale summen av alle bestillingene er: {total}\n")

maxOgDag(bestillinger)
print("\n")
overGjennomsnitt(total, bestillinger)


# Lærer: Mye bra her, William. Se mine kommentarer i koden. 




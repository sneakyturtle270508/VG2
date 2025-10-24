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

    for teller in l:
        if teller > maks:
            maks = teller

    for i in range(lengde):
        if l[i] == maks:
            index = i
        

    print(f"Dagen med flest bestillinger var {ukedager[index]} med {bestillinger[index]} bestillinger")
    return (maks, index)



#   lag funksjonen gjennomsnitt
def overGjennomsnitt(t, l):
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




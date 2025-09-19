# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-09-09 10:12:19
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-19 13:10:36

#lag en variabel som heter gangeTallet
#gi gangeTallet verdi inputt som int
gangeTallet = int(input("Hvilke gangetabbel hvil du se: "))
    #print her er gangetabbellen for: gangeTallet
print("Her er gangetabbellen for: ", gangeTallet)

#gammel løsning: 
# #lag løkke med teller som variabel som bruker tall mellom 0 og 101
# for teller in range(0, 10, gangeTallet):
#     #print teller
#     print(teller)

#forslag til løsning: 
# la teller gå fra 0 til 11
for teller in range(11):  
    # skriv hvilke tall som ganges med, skriv x, skriv gangetallet, sriv =, skriv svar av teller * gangeTallet
    print(teller, "x", gangeTallet, "=", teller * gangeTallet)
    

# Lærer: Her bruker du telleren i for-løkka på en original måte.
#        Utfordringen her her f.eks. å stoppe 6-gangen på 60, 7-gangen på 70, osv
#        Kunne dette vært gjort på en annen måte ved å la telleren i for-løkka løpe fra 1 til 10?     
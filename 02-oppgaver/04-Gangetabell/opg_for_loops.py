# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-09-09 10:12:19
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-09 10:19:49

#lag en variabel som heter gangeTallet
#gi gangeTallet verdi inputt som int
gangeTallet = int(input("Hvilke gangetabbel hvil du se"))
    #print her er gangetabbellen for: gangeTallet
print("Her er gangetabbellen for: ", gangeTallet)

#lag løkke med teller som variabel som bruker tall mellom 0 og 101
for teller in range(0, 101, gangeTallet):
    #print teller
    print(teller)
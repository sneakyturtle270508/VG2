# # -*- coding: utf-8 -*-
# # @Author: William Berge Groensberg
# # @Date:   2025-09-16 08:40:49
# # @Last Modified by:   William Berge Groensberg
# # @Last Modified time: 2025-09-19 12:33:30



# lag en diksonery for hver seddel som heter penger
# "1000" : 0
penger = {
    "1000": 0,
    "500": 0,
    "200": 0,
    "100": 0,
    "50": 0,
    "20": 0,
    "10": 0,
    "5": 0,
    "1": 0,
}
# lag variabel kjopePris og giv input og mota svar om kjøpesum
kjopePris = int(input("Hva er kjøpesummen: "))
# lag variabel betaltPris og giv input og mota svar om hvordan kunden vil betale
betaltPris = int(input("hva betaler du: "))



# lag variabel sjekkerIgjen og giv den verdi kjopePris % betaltPris
sjekkerIgjen = betaltPris % kjopePris

# Lærer: Skriv gjerne her hvor mye totalt (sjekkerIgjen) kunden skal få tilbake.

# !!!dette gjøres med alle typene med sedler!!!

# øker penger (1000) med hvor mange ganger det er 1000 lapper 
penger["1000"] += sjekkerIgjen // 1000
# sjekker verdien penger ("1000") har og ganger det med 1000 slik at det kan minuse fra 
sjekkerIgjen -= penger["1000"] * 1000

# øker penger (500) med hvor mange ganger det er 500 lapper 
penger["500"] += sjekkerIgjen // 500
# sjekker verdien penger ("500") har og ganger det med 500 slik at det kan minuse fra 
sjekkerIgjen -= penger["500"] * 500


penger["200"] += sjekkerIgjen // 200 
sjekkerIgjen -= penger["200"] * 200

penger["100"] += sjekkerIgjen // 100 
sjekkerIgjen -= penger["100"] * 100


penger["50"] += sjekkerIgjen // 50
sjekkerIgjen -= penger["50"] * 50

penger["20"] += sjekkerIgjen // 20
sjekkerIgjen -= penger["20"] * 20

penger["10"] += sjekkerIgjen // 10
sjekkerIgjen -= penger["10"] * 10

penger["5"] += sjekkerIgjen // 5
sjekkerIgjen -= penger["5"] * 5


penger["1"] += sjekkerIgjen // 1
sjekkerIgjen -= penger["1"] * 1

# print all verdiene i penger
print(f"{penger['1000']} tusen lapp(er)")
print(f"{penger['500']} fem hundre lapp(er)")
print(f"{penger['200']} to hundre lapp(er)")
print(f"{penger['100']} hundre lapp(er)")
print(f"{penger['50']} femti lapp(er)")
print(f"{penger['20']} tjue krone(r)")
print(f"{penger['10']} ti krone(r)")
print(f"{penger['5']} fem krone(r)")
print(f"{penger['1']} en krone(r)")


# Lærer: Du har løst oppgaven på en original måte. Det er bra!
#        Dersom kunden bare skulle hatt tilbake 1 krone, vil programmet ditt
#        likevel kjøre gjennom kalkulasjonene for hver eneste myntenhet fra kr 1000 til kr 1.
#        Kunne dette vært løst noe mer effektivt der du også faktisk kun printer myntenheter
#        kunden skal ha tilbake? 









# lag variabelen kontant og giv verdi 0
    
# # -*- coding: utf-8 -*-
# # @Author: William Berge Groensberg
# # @Date:   2025-09-16 08:40:49
# # @Last Modified by:   William Berge Groensberg
# # @Last Modified time: 2025-09-16 10:52:29

test = []

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
betaltPris = int(input("hva betaler du med "))



# lag variabel sjekkerIgjen og giv den verdi kjopePris % betaltPris
sjekkerIgjen = betaltPris % kjopePris



# hvis det ikke er et tall skriv til bruker du må skrive inn et tall

# eller

# !!!dette gjøres med alle typene med sedler!!!

# øker penger (1000) med hvor mange ganger det er 1000 lapper 
penger["1000"] += sjekkerIgjen // 1000
# sjekker verdien penger ("1000") har og ganger det med 1000 slik at det kan minuse fra 
sjekkerIgjen -= penger["1000"] * 1000

# øker penger (500) med hvor mange ganger det er 1000 lapper 
penger["500"] += sjekkerIgjen // 500
# sjekker verdien penger ("500") har og ganger det med 1000 slik at det kan minuse fra 
sjekkerIgjen -= penger["500"] * 500

# øker penger (200) med hvor mange ganger det er 1000 lapper 
penger["200"] += sjekkerIgjen // 200
# sjekker verdien penger ("200") har og ganger det med 1000 slik at det kan minuse fra 
sjekkerIgjen -= penger["200"] * 200

# øker penger (100) med hvor mange ganger det er 1000 lapper 
penger["100"] += sjekkerIgjen // 100
# sjekker verdien penger ("100") har og ganger det med 1000 slik at det kan minuse fra 
sjekkerIgjen -= penger["100"] * 100

# øker penger (50) med hvor mange ganger det er 1000 lapper 
penger["50"] += sjekkerIgjen // 50
# sjekker verdien penger ("50") har og ganger det med 1000 slik at det kan minuse fra 
sjekkerIgjen -= penger["50"] * 50

# øker penger (20) med hvor mange ganger det er 1000 lapper 
penger["20"] += sjekkerIgjen // 20
# sjekker verdien penger ("20") har og ganger det med 1000 slik at det kan minuse fra 
sjekkerIgjen -= penger["20"] * 20

# øker penger (10) med hvor mange ganger det er 1000 lapper 
penger["10"] += sjekkerIgjen // 10
# sjekker verdien penger ("10") har og ganger det med 1000 slik at det kan minuse fra 
sjekkerIgjen -= penger["10"] * 10

# øker penger (5) med hvor mange ganger det er 1000 lapper 
penger["5"] += sjekkerIgjen // 5
# sjekker verdien penger ("1000") har og ganger det med 1000 slik at det kan minuse fra 
sjekkerIgjen -= penger["5"] * 5


# øker penger (1) med hvor mange ganger det er 1000 lapper 
penger["1"] += sjekkerIgjen // 1
# sjekker verdien penger ("1") har og ganger det med 1000 slik at det kan minuse fra 
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









# lag variabelen kontant og giv verdi 0
    
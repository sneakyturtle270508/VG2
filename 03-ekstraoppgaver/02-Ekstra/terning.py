# # -*- coding: utf-8 -*-
# # @Author: William Berge Groensberg
# # @Date:   2025-08-28 20:08:01
# # @Last Modified by:   William Berge Groensberg
# # @Last Modified time: 2025-09-05 12:46:46

# importere random
import random
# importere tiden
import time

# lag variabel terningen
# gi terningen verdi random med et tall fra 1 til 6
terningen = random.randint(1, 6)
# lag variabel antall_ganger_trillet
# gi antall_ganger_trillet verdi 1
antall_ganger_trillet = 1
 
# skriv hvor mange forsøk bruker du på å få tallet 6 på terningen
print("Hvor mange forsøk bruker du på å få tallet 6 på terningen.")
# vent tre sekunder
time.sleep(1)
print("triller...")
time.sleep(2)


# skriv forsøk og antall_ganger_trillet som nr på forsøkt
# skriv verdien til terningen
print(f"forsøk nr.{antall_ganger_trillet}\nterningen viser: {terningen}")

# hvis ikke det er nr 6
#     plusser antall_ganger_trillet med 1
#     skriv trykk på enter for å trille på nytt
# hvis enter trykkes 
#     skriv ny verdi til terningen    

while terningen != 6:  #while kjører som if/else men den kjører så lenge svaret ikke er tallet 6
    antall_ganger_trillet += 1
    input("\nTrykk Enter for å trille på nytt...")  #input venter på enter
    terningen = random.randint(1, 6)
    time.sleep(1)
    print("triller...")
    time.sleep(2)
    print(f"Forsøk nr.{antall_ganger_trillet}\nTerningen viser: {terningen}")

# hvis tallet er 6 
#     skriv gratulere du vant
#     skriv du brukte: antall forsøk

print(f"\nGratulerer, du vant\ndu brukte {antall_ganger_trillet} forsøk")
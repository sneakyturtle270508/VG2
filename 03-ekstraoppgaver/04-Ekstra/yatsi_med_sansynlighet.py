# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-09-05 19:57:19
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-05 20:43:54

# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-08-29 14:37:59
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-05 20:27:35

# importer random
# importer time
import random
import time

antall_simuleringer = int(input("Hvor mange ganger vil du prøve å få Yatzy? "))
totale_kast = 0

# print prøv å få Yatzy med 5 terninger!
print("prøv å få Yatzy med 5 terninger!")

for i in range(antall_simuleringer):
    antall_forsok = 0
    # mens vi ikke har fått Yatzy: #løkke uten autoinkrement så den stopper ikke
    while True:
    #     Øk antall_forsøk med 1
        antall_forsok += 1
    #     Be bruker trykke Enter for å trille
        # input("Trykk Enter for å trille terningene...")
        

    #     Kast/lag variabel terning 1 (tilfeldig tall 1-6)
        t1 = random.randint(1, 6)

    #     Kast/lag variabel terning 2 (tilfeldig tall 1-6)
        t2 = random.randint(1, 6)

    #     Kast/lag variabel terning 3 (tilfeldig tall 1-6)
        t3 = random.randint(1, 6)

    #     Kast/lag variabel terning 4 (tilfeldig tall 1-6)
        t4 = random.randint(1, 6)

    #     Kast/lag variabel terning 5 (tilfeldig tall 1-6)
        t5 = random.randint(1, 6)


    #     print terning 1 (tilfeldig tall 1-6)
        print("Terning 1:", t1)

    #     print terning 2 (tilfeldig tall 1-6)
        print("Terning 2:", t2)

    #     print terning 3 (tilfeldig tall 1-6)
        print("Terning 3:", t3)

    #     print terning 4 (tilfeldig tall 1-6)
        print("Terning 4:", t4)

    #     print terning 5 (tilfeldig tall 1-6)
        print("Terning 5:", t5)

    #     Hvis alle terningene er like:  
        if t1 == t2 == t3 == t4 == t5:
    #         Stopp løkken (Yatzy er oppnådd)
            totale_kast += antall_forsok
            break
    #     Ellers:
        else:
#         Skriv ut "Ingen Yatzy denne gangen, prøv igjen!"
# 
            print(f"Ingen Yatzy denne gangen, prøv igjen! \nDu har brukt {antall_forsok}")
#         Vent 1 sekund
        # time.sleep(1)

# print Yatzy! Det tok {antall_forsøk} forsøk å få alle like.
gjennomsnitt = totale_kast / antall_simuleringer

print(f"gannger kjørte tester: {antall_simuleringer} | mest sansynlig tar det round: {gjennomsnitt}")



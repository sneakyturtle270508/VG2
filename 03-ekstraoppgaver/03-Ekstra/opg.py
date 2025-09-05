# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-08-29 12:24:02
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-03 20:40:55


# importer random
import random
# importer time
import time

# lag variabel terning1
# gi variabelen terning1 verdien random tall
terning1 = random.randint(1, 6)

# lag variabelen terning2
# gi variabelen terning2 verdien random tall
terning2 = random.randint(1, 6)

# lag variabelen antall_trillet 
# gi variablen verdi 0
antall_trillet = 0


# skriv hvor mange like kan du få...
print("hvor mange trill bruker du på å få 2 like...")



while terning1 != terning2:
        antall_trillet += 1
        input("klikk Enter for å trille...")
        terning1 = random.randint(1,6)
        terning2 = random.randint(1,6)
        time.sleep(1)
        print("triller...")
        time.sleep(1)
        # skriv verdi til terning1
        print(f"terning Nr.1: {terning1}")
        # skriv verdi til terning2
        print(f"terning Nr.2: {terning2}")
        print(f"antall forsøk: {antall_trillet}")

# hvis terning1 er samme som terning2
# skriv det tok antall forsøk: antall_forsøk
print(f"det tok {antall_trillet} antall forsøk")
# skriv trykk enter for å trille på nytt...
input("start programmet på nytt for å starte nytt spill.")

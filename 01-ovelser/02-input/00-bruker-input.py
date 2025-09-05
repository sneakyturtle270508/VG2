# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-08-27 13:23:06
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-08-27 13:49:21
alder = int(input("skriv in alderen din: "))# vi lager en variabel med tallet 19


if alder >= 18:         # sjekker om alder er større enn eller lik 18
    print("du er myndig, og kan stemme")   # hvis det stemmer -> skriv ut denne teksten
elif alder >= 16:
    print("ikke myndig, men skolevalget går")
else:                   # ellers, hvis det IKKE stemmer
    print("ikke myndig, kan ikke stemme ")    # da skrives denne teksten



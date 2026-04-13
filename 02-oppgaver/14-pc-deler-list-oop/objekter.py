# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-12 18:23:44
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-13 23:51:44


# ============================================================
# SUPERKLASSE
# ============================================================



from prosessor import Prosessor
from grafikkort import Grafikkort
from ram import Ram


cpu1 = Prosessor("Intel", "Core i7-12700K", 1500, 800, 1500, "god", 12, 3.6)
cpu2 = Prosessor("AMD", "Ryzen 5 5600X", 900, 500, 900, "slitt", 6, 3.7)

gpu1 = Grafikkort("Nvidia", "RTX 3080", 4000, 2500, 4000, "god", 10, "GDDR6X")
gpu2 = Grafikkort("AMD", "RX 6700 XT", 2500, 1500, 2500, "god", 12, "GDDR6")

ram1 = Ram("Corsair", "Vengeance", 600, 300, 600, "god", 16, 3200)
ram2 = Ram("Kingston", "Fury", 900, 500, 900, "slitt", 32, 3600)


# ============================================================
# LISTE + LOOP
# ============================================================

alle_deler = [cpu1, cpu2, gpu1, gpu2, ram1, ram2]


for x in alle_deler:
    print("----------------------------")
    x.vis_komponent()
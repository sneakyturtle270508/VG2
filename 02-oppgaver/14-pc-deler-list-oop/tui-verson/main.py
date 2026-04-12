# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-07 11:09:18
# @Last Modified by:   William Berge Groensberg

import os
from meny import*

# ANSI farger
GRN = "\033[32m"
CYN = "\033[36m"
YLW = "\033[33m"
RED = "\033[31m"
WHT = "\033[97m"
RST = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def header():
    print(GRN + """               /$$   /$$     /$$           /$$                                           /$$                        
              |__/  | $$    | $$          |__/                                          | $$                        
 /$$$$$$/$$$$  /$$ /$$$$$$ /$$$$$$         /$$ /$$$$$$$  /$$    /$$ /$$$$$$  /$$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
| $$_  $$_  $$| $$|_  $$_/|_  $$_/        | $$| $$__  $$|  $$  /$$//$$__  $$| $$__  $$|_  $$_/   |____  $$ /$$__  $$
| $$ \ $$ \ $$| $$  | $$    | $$          | $$| $$  \ $$ \  $$/$$/| $$$$$$$$| $$  \ $$  | $$      /$$$$$$$| $$  \__/
| $$ | $$ | $$| $$  | $$ /$$| $$ /$$      | $$| $$  | $$  \  $$$/ | $$_____/| $$  | $$  | $$ /$$ /$$__  $$| $$      
| $$ | $$ | $$| $$  |  $$$$/|  $$$$/      | $$| $$  | $$   \  $/  |  $$$$$$$| $$  | $$  |  $$$$/|  $$$$$$$| $$      
|__/ |__/ |__/|__/   \___/   \___/        |__/|__/  |__/    \_/    \_______/|__/  |__/   \___/   \_______/|__/""" + RST)



# ============================================================
# Superklassen Pc
# ============================================================

class Pc:
    def __init__(self, merke, modell, inkjopspris, forventet_pris, tilstand, solgt, solgt_for=None):
        self.merke = merke
        self.modell = modell
        self.inkjopspris = inkjopspris
        self.forventet_pris = forventet_pris
        self.tilstand = tilstand
        self.solgt = solgt
        self.solgt_for = solgt_for

    def vis_komponent(self):
        print("  merke:          ", self.merke)
        print("  modell:         ", self.modell)
        print("  inkjøpspris:    ", self.inkjopspris, "kr")
        print("  forventet pris: ", self.forventet_pris, "kr")
        print("  tilstand:       ", self.tilstand)
        if self.solgt:
            print(GRN + "  solgt for:      ", self.solgt_for, "kr" + RST)
        else:
            print(YLW + "  status:          Ikke solgt enda" + RST)

    def fortjeneste(self):
        if self.solgt and self.solgt_for is not None:
            return self.solgt_for - self.inkjopspris
        return None


# ============================================================
# Subklassen Prosessor
# ============================================================

class Prosessor(Pc):
    def __init__(self, merke, modell, inkjopspris, forventet_pris, tilstand, solgt, antall_kjerner, klokkefrekvens, solgt_for=None):
        super().__init__(merke, modell, inkjopspris, forventet_pris, tilstand, solgt, solgt_for)
        self.antall_kjerner = antall_kjerner
        self.klokkefrekvens = klokkefrekvens

    def vis_komponent(self):
        super().vis_komponent()
        print("  antall kjerner: ", self.antall_kjerner)
        print("  klokkefrekvens: ", self.klokkefrekvens, "GHz")


# ============================================================
# Subklassen Grafikkort
# ============================================================

class Grafikkort(Pc):
    def __init__(self, merke, modell, inkjopspris, forventet_pris, tilstand, solgt, vram_gb, minnetype, solgt_for=None):
        super().__init__(merke, modell, inkjopspris, forventet_pris, tilstand, solgt, solgt_for)
        self.vram_gb = vram_gb
        self.minnetype = minnetype

    def vis_komponent(self):
        super().vis_komponent()
        print("  vram:           ", self.vram_gb, "GB")
        print("  minnetype:      ", self.minnetype)


# ============================================================
# Subklassen RAM
# ============================================================

class Ram(Pc):
    def __init__(self, merke, modell, inkjopspris, forventet_pris, tilstand, solgt, kapasitet_gb, hastighet_mhz, solgt_for=None):
        super().__init__(merke, modell, inkjopspris, forventet_pris, tilstand, solgt, solgt_for)
        self.kapasitet_gb = kapasitet_gb
        self.hastighet_mhz = hastighet_mhz

    def vis_komponent(self):
        super().vis_komponent()
        print("  kapasitet:      ", self.kapasitet_gb, "GB")
        print("  hastighet:      ", self.hastighet_mhz, "MHz")


# ============================================================
# Objekter
# ============================================================

cpu1 = Prosessor("Intel", "Core i7-12700K", 800,  1500, "god",   True,  12, 3.6, solgt_for=1500)
cpu2 = Prosessor("AMD",   "Ryzen 5 5600X",  500,  900,  "slitt", False, 6,  3.7)

gpu1 = Grafikkort("Nvidia", "RTX 3080",   2500, 4000, "god", True,  10, "GDDR6X", solgt_for=4000)
gpu2 = Grafikkort("AMD",    "RX 6700 XT", 1500, 2500, "god", False, 12, "GDDR6")

ram1 = Ram("Corsair",  "Vengeance 16GB", 300, 600, "god",   False, 16, 3200)
ram2 = Ram("Kingston", "Fury 32GB",      500, 900, "slitt", True,  32, 3600, solgt_for=900)

alle_deler = [cpu1, cpu2, gpu1, gpu2, ram1, ram2]
cpu = [cpu1, cpu2]
gpu = [gpu1, gpu2]
ram = [ram1, ram2]

def registrer_komponent():
    clear()
    header()
    print(YLW + "\n  Velg kategori:\n" + RST)
    
    kat_valg = ["CPU", "GPU", "RAM"]
    idx = pil_meny(kat_valg)
    
    clear()
    header()
    
    # Felles felter
    print(YLW + f"\n  Registrer ny {kat_valg[idx]}:\n" + RST)
    merke = input(WHT + "  Merke: " + RST)
    modell = input(WHT + "  Modell: " + RST)
    inkjopspris = int(input(WHT + "  Innkjøpspris (kr): " + RST))
    forventet_pris = int(input(WHT + "  Forventet salgspris (kr): " + RST))
    tilstand = input(WHT + "  Tilstand (god/slitt): " + RST)
    
    # Kategori-spesifikke felter
    if idx == 0:  # CPU
        antall_kjerner = int(input(WHT + "  Antall kjerner: " + RST))
        klokkefrekvens = float(input(WHT + "  Klokkefrekvens (GHz): " + RST))
        ny = Prosessor(merke, modell, inkjopspris, forventet_pris, tilstand, False, None, antall_kjerner, klokkefrekvens)
        cpu.append(ny)
    elif idx == 1:  # GPU
        vram_gb = int(input(WHT + "  VRAM (GB): " + RST))
        minnetype = input(WHT + "  Minnetype (f.eks GDDR6): " + RST)
        ny = Grafikkort(merke, modell, inkjopspris, forventet_pris, tilstand, False, None, vram_gb, minnetype)
        gpu.append(ny)
    elif idx == 2:  # RAM
        kapasitet_gb = int(input(WHT + "  Kapasitet (GB): " + RST))
        hastighet_mhz = int(input(WHT + "  Hastighet (MHz): " + RST))
        ny = Ram(merke, modell, inkjopspris, forventet_pris, tilstand, False, None, kapasitet_gb, hastighet_mhz)
        ram.append(ny)
    
    alle_deler.append(ny)
    print(GRN + f"\n  ✔ {kat_valg[idx]} registrert!" + RST)
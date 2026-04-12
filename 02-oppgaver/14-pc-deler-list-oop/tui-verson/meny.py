# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-12 01:17:08
# @Last Modified by:   William Berge Groensberg

import msvcrt
from main import *


# ============================================================
# Piltast-navigasjon
# ============================================================

def velg_fra_meny(valg_liste):
    valgt = 0
    while True:
        for i, val in enumerate(valg_liste):
            if i == valgt:
                print(CYN + f"> {val}" + RST)
            else:
                print(WHT + f"    {val}" + RST)

        tast = msvcrt.getch()

        if tast == b'\xe0':
            tast2 = msvcrt.getch()
            if tast2 == b'H':
                valgt = (valgt - 1) % len(valg_liste)
            elif tast2 == b'P':
                valgt = (valgt + 1) % len(valg_liste)
        elif tast == b'\r':
            return valgt
        elif tast in [b'1', b'2', b'3', b'4', b'0']:
            num = int(tast.decode())
            if 0 < num <= len(valg_liste):
                return num - 1
            elif num == 0:
                return len(valg_liste) - 1

        for _ in valg_liste:
            print("\033[F\033[K", end="")


# ============================================================
# Hjelpefunksjoner
# ============================================================

def vis_komponent_pent(komponent):
    print(CYN + "╔══════════════════════════════════════════╗" + RST)
    komponent.vis_komponent()
    print(CYN + "╚══════════════════════════════════════════╝" + RST)


def registrer_komponent():
    clear()
    header()
    print(YLW + "\n  Velg kategori:\n" + RST)

    kat_liste = ["CPU", "GPU", "RAM", "Avbryt"]
    kat = velg_fra_meny(kat_liste)

    if kat == 3:
        return

    clear()
    header()
    print(YLW + f"\n  Registrer ny {kat_liste[kat]}:\n" + RST)

    merke          = input(WHT + "  Merke:                    " + RST)
    modell         = input(WHT + "  Modell:                   " + RST)
    inkjopspris    = int(input(WHT + "  Innkjøpspris (kr):       " + RST))
    forventet_pris = int(input(WHT + "  Forventet salgspris (kr):" + RST))
    tilstand       = input(WHT + "  Tilstand (god/slitt):     " + RST)

    if kat == 0:  # CPU
        antall_kjerner = int(input(WHT + "  Antall kjerner:          " + RST))
        klokkefrekvens = float(input(WHT + "  Klokkefrekvens (GHz):    " + RST))
        ny = Prosessor(merke, modell, inkjopspris, forventet_pris, tilstand, False, None, antall_kjerner, klokkefrekvens)
        cpu.append(ny)

    elif kat == 1:  # GPU
        vram_gb    = int(input(WHT + "  VRAM (GB):                " + RST))
        minnetype  = input(WHT + "  Minnetype (f.eks GDDR6):  " + RST)
        ny = Grafikkort(merke, modell, inkjopspris, forventet_pris, tilstand, False, None, vram_gb, minnetype)
        gpu.append(ny)

    elif kat == 2:  # RAM
        kapasitet_gb  = int(input(WHT + "  Kapasitet (GB):           " + RST))
        hastighet_mhz = int(input(WHT + "  Hastighet (MHz):          " + RST))
        ny = Ram(merke, modell, inkjopspris, forventet_pris, tilstand, False, None, kapasitet_gb, hastighet_mhz)
        ram.append(ny)

    alle_deler.append(ny)
    print(GRN + f"\n  ✔ {kat_liste[kat]} lagt til!\n" + RST)


# ============================================================
# Meny
# ============================================================

hoved_valg     = ["1. Se alle komponenter", "2. Regnskap", "3. Kategorier", "4. Registrer ny", "0. Avslutt"]
kategori_valg  = ["1. CPU", "2. GPU", "3. RAM", "Tilbake"]

while True:
    clear()
    header()
    print(WHT + "\n  Bruk piltaster eller tall:\n" + RST)

    valgt = velg_fra_meny(hoved_valg)

    if valgt == 0:  # Se alle
        clear()
        header()
        print(YLW + "\n  Alle komponenter:\n" + RST)
        for komponent in alle_deler:
            vis_komponent_pent(komponent)

    elif valgt == 1:  # Regnskap
        clear()
        header()
        print(YLW + "\n  Regnskap:\n" + RST)

        total_inkjop   = sum(k.inkjopspris for k in alle_deler)
        total_solgt    = sum(k.solgt_for for k in alle_deler if k.solgt and k.solgt_for is not None)
        fortjeneste    = total_solgt - total_inkjop
        farge          = GRN if fortjeneste >= 0 else RED

        print(CYN + "╔══════════════════════════════════════════╗")
        print(      "║            Oversikt                      ║")
        print(      "╚══════════════════════════════════════════╝" + RST)
        print(RED + f"  Totalt inkjøp:      {total_inkjop} kr" + RST)
        print(GRN + f"  Totalt solgt for:   {total_solgt} kr" + RST)
        print(farge + f"  Fortjeneste:        {fortjeneste} kr" + RST)

    elif valgt == 2:  # Kategorier
        clear()
        header()
        print(YLW + "\n  Velg kategori:\n" + RST)

        kat = velg_fra_meny(kategori_valg)

        if kat == 3:
            continue

        clear()
        header()
        if kat == 0:
            print(YLW + "\n  CPU-er:\n" + RST)
            for komponent in cpu:
                vis_komponent_pent(komponent)
        elif kat == 1:
            print(YLW + "\n  Grafikkort:\n" + RST)
            for komponent in gpu:
                vis_komponent_pent(komponent)
        elif kat == 2:
            print(YLW + "\n  RAM:\n" + RST)
            for komponent in ram:
                vis_komponent_pent(komponent)

    elif valgt == 3:  # Registrer ny
        registrer_komponent()

    elif valgt == 4:  # Avslutt
        clear()
        print(GRN + "\n  Avslutter... Ha en fin dag!\n" + RST)
        break

    input(CYN + "\n  Trykk Enter for å gå tilbake..." + RST)
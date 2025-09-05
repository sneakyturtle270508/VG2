# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-09-03 13:29:14
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-03 13:31:03
import random


antall_forsok = 0

print("Prøv å få Yatzy med 5 terninger!")

# laget av chatgpt ----------------------------

# ASCII-art for terningene
dice_art = {
    1: (
        "┌─────┐\n"
        "│     │\n"
        "│  •  │\n"
        "│     │\n"
        "└─────┘"
    ),
    2: (
        "┌─────┐\n"
        "│ •   │\n"
        "│     │\n"
        "│   • │\n"
        "└─────┘"
    ),
    3: (
        "┌─────┐\n"
        "│ •   │\n"
        "│  •  │\n"
        "│   • │\n"
        "└─────┘"
    ),
    4: (
        "┌─────┐\n"
        "│ • • │\n"
        "│     │\n"
        "│ • • │\n"
        "└─────┘"
    ),
    5: (
        "┌─────┐\n"
        "│ • • │\n"
        "│  •  │\n"
        "│ • • │\n"
        "└─────┘"
    ),
    6: (
        "┌─────┐\n"
        "│ • • │\n"
        "│ • • │\n"
        "│ • • │\n"
        "└─────┘"
    )
}

# Funksjon for å printe flere terninger side om side
def print_dice(dice_list):
    dice_lines = [""] * 5
    for value in dice_list:
        art_lines = dice_art[value].split("\n")
        for i in range(5):
            dice_lines[i] += art_lines[i] + "  "
    print("\n".join(dice_lines))

# -------------------------------------------------------

while True:
    antall_forsok += 1
    input("Trykk Enter for å trille terningene...")

    t1 = random.randint(1, 6)
    t2 = random.randint(1, 6)
    t3 = random.randint(1, 6)
    t4 = random.randint(1, 6)
    t5 = random.randint(1, 6)

    dice_list = [t1, t2, t3, t4, t5]

    # Print ASCII-terningene
    print_dice(dice_list)

    if t1 == t2 == t3 == t4 == t5:
        break
    else:
        print(f"Ingen Yatzy denne gangen, prøv igjen! \nDu har brukt {antall_forsok} forsøk\n")
        # time.sleep(1)

print(f"Yatzy! Det tok {antall_forsok} forsøk å få alle like.")

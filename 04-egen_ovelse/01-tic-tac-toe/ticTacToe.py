# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-09-11 14:16:31
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-14 18:36:04
# initialisering
board = [1,2,3,4,5,6,7,8,9]
spiller1 = []
spiller2 = []

winning_combo = [
    {1,2,3}, {4,5,6}, {7,8,9},
    {1,4,7}, {2,5,8}, {3,6,9},
    {1,5,9}, {3,5,7},
]

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\nSpiller 1: ", spiller1)
    print("Spiller 2: ", spiller2)
    print("\n")  # ekstra linje for å gjøre det ryddig

while True:
    print_board()
    
    # Spiller 1
    valgt_tall = int(input("Spiller 1, velg tall: "))
    if valgt_tall not in board:
        print("Ugyldig trekk, prøv igjen.")
        continue
    spiller1.append(valgt_tall)
    board[board.index(valgt_tall)] = 'X'
    
    if any(combo.issubset(spiller1) for combo in winning_combo):
        print_board()
        print("Spiller 1 vant!")
        break

    # Sjekk for uavgjort
    if all(isinstance(x, str) for x in board):
        print_board()
        print("Uavgjort!")
        break

    # Spiller 2
    print_board()
    valgt_tall = int(input("Spiller 2, velg tall: "))
    if valgt_tall not in board:
        print("Ugyldig trekk, prøv igjen.")
        continue
    spiller2.append(valgt_tall)
    board[board.index(valgt_tall)] = 'O'
    
    if any(combo.issubset(spiller2) for combo in winning_combo):
        print_board()
        print("Spiller 2 vant!")
        break

    # Sjekk for uavgjort igjen
    if all(isinstance(x, str) for x in board):
        print_board()
        print("Uavgjort!")
        break

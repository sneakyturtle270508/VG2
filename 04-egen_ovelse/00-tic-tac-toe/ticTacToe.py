# # -*- coding: utf-8 -*-
# # @Author: William Berge Groensberg
# # @Date:   2025-09-11 14:16:31
# # @Last Modified by:   William Berge Groensberg
# # @Last Modified time: 2025-09-11 15:01:44


player1Score = 0 
player2Score = 0
drawScore = 0

spiller1 = []
spiller2 = []
board = [1,2,3,4,5,6,7,8,9]

winning_combo = [
    {1,2,3},
    {4,5,6},
    {7,8,9},
    {1,4,7},
    {2,5,8},
    {3,6,9},
    {1,5,9},
    {3,5,7},
]

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

while True:
    # Spiller 1
    print_board()
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
    if all(isinstance(x, str) for x in board):
        print_board()
        print("Uavgjort!")
        break
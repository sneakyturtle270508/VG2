# -*- coding: utf-8 -*- 
# @Author: William Berge Groensberg
# @Date:   2025-09-18 14:12:06
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-19 12:27:32
import random

# Lag kortstokk
def create_deck():
    suits = ['♠', '♥', '♦', '♣']
    values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    deck = [v + s for v in values for s in suits]
    random.shuffle(deck)
    return deck

# Tegn kortene som ASCII-art
def draw_card(card):
    v, s = card[:-1], card[-1]
    return [
        "┌───────┐",
        f"|{v:<2}     |",
        f"|   {s}   |",
        f"|     {v:>2}|",
        "└───────┘"
    ]

def draw_hand(cards):
    lines = [draw_card(c) for c in cards]
    hand_ascii = "\n".join("  ".join(card[i] for card in lines) for i in range(5))
    return hand_ascii + f"\n\nTotal verdi: {hand_value(cards)}"

def hand_value(hand):
    value = 0
    aces = 0
    
    for card in hand:
        v = card[:-1]   # everything except last char (suit)
        
        if v in ["J", "Q", "K"]:
            value += 10
        elif v == "A":
            value += 11   # count Ace as 11 for now
            aces += 1
        else:
            value += int(v)

    # Adjust Aces (turn 11 into 1 if we go over 21)
    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value

# Start
deck = create_deck()
hand = [deck.pop(), deck.pop()]

print(draw_hand(hand))

while True:
    if hand_value(hand) > 21:
        print("\nDu bustet!")
        break
    elif hand_value(hand) == 21:
        print("blackjack")
        break

    valg = input("\nTast 1 for å trekke et kort\nTast 2 for å stoppe\n> ")

    if valg == "1":
        hand.append(deck.pop())
        print(draw_hand(hand))

    elif valg == "2":
        print("\nDin endelige hånd:")
        print(draw_hand(hand))
        break

    else:
        print("Ugyldig valg, prøv igjen.")

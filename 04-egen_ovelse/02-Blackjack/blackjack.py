# -*- coding: utf-8 -*- 
# @Author: William Berge Groensberg
# @Date:   2025-09-18 14:12:06
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-19 15:43:06

import random
import time
import os

def create_deck():
    suits = ['♠', '♥', '♦', '♣']
    values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    deck = [v + s for v in values for s in suits]
    random.shuffle(deck)
    return deck

def draw_card(card):
    v, s = card[:-1], card[-1]
    return [
        "┌───────┐",
        f"|{v:<2}     |",
        f"|   {s}   |",
        f"|     {v:>2}|",
        "└───────┘"
    ]

def draw_hand(cards, show_value=True):
    lines = [draw_card(c) for c in cards]
    hand_ascii = "\n".join("  ".join(card[i] for card in lines) for i in range(5))
    if show_value:
        return hand_ascii + f"\n\nTotal verdi: {hand_value(cards)}"
    return hand_ascii

def draw_hidden_dealer_hand(dealer_hand, flip_stage=0):
    visible = draw_card(dealer_hand[0])

    hidden_frames = {
        0: [  # skjult
            "┌───────┐",
            "|░░░░░░░|",
            "|░░░░░░░|",
            "|░░░░░░░|",
            "└───────┘"
        ],
        1: [  # halvveis flip
            "┌───────┐",
            "|///    |",
            "|   /// |",
            "|    ///|",
            "└───────┘"
        ],
        2: draw_card(dealer_hand[1])  # ekte kort
    }

    hidden = hidden_frames[flip_stage]
    lines = [visible, hidden]
    return "\n".join("  ".join(card[i] for card in lines) for i in range(5))

def hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        v = card[:-1]
        if v in ["J", "Q", "K"]:
            value += 10
        elif v == "A":
            value += 11
            aces += 1
        else:
            value += int(v)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def show_table(player_hand, dealer_hand, hide_dealer=True, flip_stage=0):
    os.system("cls" if os.name == "nt" else "clear")
    print("=== DEALER ===")
    if hide_dealer:
        print(draw_hidden_dealer_hand(dealer_hand, flip_stage))
    else:
        print(draw_hand(dealer_hand))
    print("\n=== DU ===")
    print(draw_hand(player_hand))

def flip_dealer_card(player_hand, dealer_hand):
    # Kjør animasjon (fra skjult → halvveis → ekte)
    for stage in [0, 1, 2]:
        show_table(player_hand, dealer_hand, hide_dealer=True, flip_stage=stage)
        time.sleep(0.6)


# ------------------------------
# Start spillet
deck = create_deck()
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

show_table(player_hand, dealer_hand, hide_dealer=True)

while True:
    if hand_value(player_hand) > 21:
        print("\nDu bustet! Dealer vinner.")
        break
    elif hand_value(player_hand) == 21:
        print("\nBlackjack! 😎")
        break

    valg = input("\nTast 1 for å trekke et kort\nTast 2 for å stoppe\n> ")

    if valg == "1":
        player_hand.append(deck.pop())
        show_table(player_hand, dealer_hand, hide_dealer=True)

    elif valg == "2":
        # Flipp dealerens skjulte kort med animasjon
        flip_dealer_card(player_hand, dealer_hand)

        # Deretter spill dealerens tur
        while hand_value(dealer_hand) < 17:
            dealer_hand.append(deck.pop())
            show_table(player_hand, dealer_hand, hide_dealer=False)
            time.sleep(1)

        # Resultat
        player_total = hand_value(player_hand)
        dealer_total = hand_value(dealer_hand)

        if dealer_total > 21 or player_total > dealer_total:
            print("\nDu vinner! 🎉")
        elif player_total < dealer_total:
            print("\nDealer vinner!")
        else:
            print("\nDealer er verdt mer og vinner")
        break

    else:
        print("Ugyldig valg, prøv igjen.")

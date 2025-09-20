# -*- coding: utf-8 -*- 
# @Author: William Berge Groensberg
# @Date:   2025-09-18 14:12:06
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-19 18:45:44

import random
import time
import os

# ------------------------------
# Pengebeholdning
pengebok = 100

# ------------------------------
# Kortstokk
def create_deck():
    suits = ['♠', '♥', '♦', '♣']
    values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    deck = [v + s for v in values for s in suits]
    random.shuffle(deck)
    return deck

# ASCII-kort
def draw_card(card):
    v, s = card[:-1], card[-1]
    return [
        "┌───────┐",
        f"|{v:<2}     |",
        f"|   {s}   |",
        f"|     {v:>2}|",
        "└───────┘"
    ]

# Tegn hånd
def draw_hand(cards, show_value=True):
    lines = [draw_card(c) for c in cards]
    hand_ascii = "\n".join("  ".join(card[i] for card in lines) for i in range(5))
    if show_value:
        return hand_ascii + f"\n\nTotal verdi: {hand_value(cards)}"
    return hand_ascii

# Dealer hånd med skjult kort
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

# ------------------------------
# Verdien av en hånd
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

# ------------------------------
# Vis bordet
def show_table(player_hand, dealer_hand, hide_dealer=True, flip_stage=0):
    os.system("cls" if os.name == "nt" else "clear")
    print("=== DEALER ===")
    if hide_dealer:
        print(draw_hidden_dealer_hand(dealer_hand, flip_stage))
    else:
        print(draw_hand(dealer_hand))
    print("\n=== DU ===")
    print(draw_hand(player_hand))
    print(f"\nPengebeholdning: {pengebok} chips")

# ------------------------------
# Dealer flip animasjon
def flip_dealer_card(player_hand, dealer_hand):
    for stage in [0,1,2]:
        show_table(player_hand, dealer_hand, hide_dealer=True, flip_stage=stage)
        time.sleep(0.6)

# ------------------------------
# Funksjon for innsats
def place_bet():
    global pengebok
    if pengebok <= 0:
        print("Du har 0 chips! Ny start med 100 chips.")
        pengebok = 100
    while True:
        try:
            bet = int(input(f"Din pengebeholdning: {pengebok}. Hvor mye vil du satse? "))
            if bet <= pengebok and bet > 0:
                return bet
            else:
                print("Ugyldig beløp, prøv igjen.")
        except ValueError:
            print("Skriv et gyldig tall.")

# ------------------------------
# Hovedspill-loop
while True:
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    bet = place_bet()
    show_table(player_hand, dealer_hand, hide_dealer=True)

    # Spillerens tur
    while True:
        if hand_value(player_hand) > 21:
            show_table(player_hand, dealer_hand, hide_dealer=False)
            print(f"\nDu bustet! -{bet} chips")
            pengebok -= bet
            break
        elif hand_value(player_hand) == 21:
            show_table(player_hand, dealer_hand, hide_dealer=False)
            print(f"\nBlackjack! +{int(bet*1.5)} chips")
            pengebok += int(bet*1.5)
            break

        valg = input("\nTast 1 for å trekke et kort\nTast 2 for å stoppe\n> ")

        if valg == "1":
            player_hand.append(deck.pop())
            show_table(player_hand, dealer_hand, hide_dealer=True)

        elif valg == "2":
            flip_dealer_card(player_hand, dealer_hand)
            # Dealerens tur
            while hand_value(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
                show_table(player_hand, dealer_hand, hide_dealer=False)
                time.sleep(1)

            # Resultat
            dealer_total = hand_value(dealer_hand)
            player_total = hand_value(player_hand)

            if dealer_total > 21 or player_total > dealer_total:
                print(f"\nDu vinner! +{bet} chips")
                pengebok += bet
            elif player_total < dealer_total:
                print(f"\nDealer vinner! -{bet} chips")
                pengebok -= bet
            else:
                print(f"\nUavgjort! Du får tilbake innsatsen: {bet} chips")

            break

    # Spør om ny runde
    cont = input("\nVil du spille en ny runde? (j/n) > ").lower()
    if cont != "j":
        print(f"Du slutter med {pengebok} chips. Ha det!")
        break

# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-09-02 10:22:33
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-02 11:19:41
 
# opg - innhold
# bruker får 10 spørsmål som bruker svarer på
# gi bruker tilbake meding i form av riktig eller galt
# telle opp rette svar 

# ---------------------------------------------------
# lag variabelen poengTeller
# gi verdi 0 til variabelen poengTeller
poengTeller = 0
# lag variabelen poengTellerMotsatt
# gi verdi 0 til variabelen poengTellerMotsatt
poengTellerMotsatt = 0
# ---------------------------------------------------
# lag s1 til s10 og legg in et spørsmål pr som str

# s1 = hva er hovedstaden i norge: oslo
s1 = "hva er hovedstaden i norge:"
# s2 = hvilke programmeringspråk bruker KI : python
s2 = "hvilke programmeringspråk bruker KI:"
# s3 = hva er filformatet(eksempel: .exe) til en tekstfil: .txt
s3 = "hva er filformatet(eksempel: .exe) til en tekstfil:"
# s4 = hva heter jeg som lagde dette: William
s4 = "hva heter jeg som lagde dette:"
# s5 = hva er min alder: 17
s5 = "hva er min alder:"
# s6 = puster du: ja
s6 = "puster du:"
# s7 = bruker du vs code nå : ja
s7 = "bruker du vs code nå:"
# s8 = liker jeg(William) noe annet en oneplus som tlf: ja
s8 = "liker jeg(William) noe annet en oneplus som tlf:"
# s9 = bruker du windows nå: ja
s9= "bruker du windows nå:"
# s10 = bruker du en skjerm for å se på dette: ja
s10 = "bruker du en skjerm for å se på dette:"
# ----------------------------------------------------
# print du trenger bare å svare med et ord
print("du trenger bare å svare med et ord!")
# print s1 og gi bruker muliget til inputt

# ta imot svar
svar1 = input(s1 + " ")
# hvis  input fra bruker er svar oslo
if svar1.lower() == "oslo":
#     øk verdien til poengTeller med 1
    poengTeller += 1
    print(f"du fikk riktig")
# eller
else:
#     øk verdien til poengTellerMotsatt med 1
    poengTellerMotsatt +=1
    print("du fikk feil")
# print -----------------------------------
print("____________________________________")


# ta imot svar
svar2 = input(s2 + " ")
# hvis  input fra bruker er svar oslo
if svar2.lower() == "python":
#     øk verdien til poengTeller med 1
    poengTeller += 1
    print(f"du fikk riktig")
# eller
else:
#     øk verdien til poengTellerMotsatt med 1
    poengTellerMotsatt +=1
    print("du fikk feil")
# print -----------------------------------
print("____________________________________")


# ta imot svar
svar3 = input(s3 + " ")
# hvis  input fra bruker er svar oslo
if svar3.lower() == ".txt":
#     øk verdien til poengTeller med 1
    poengTeller += 1
    print(f"du fikk riktig")
# eller
else:
#     øk verdien til poengTellerMotsatt med 1
    poengTellerMotsatt +=1
    print("du fikk feil")
# print -----------------------------------
print("____________________________________")


# ta imot svar
svar4 = input(s4 + " ")
# hvis  input fra bruker er svar oslo
if svar4.lower() == "william":
#     øk verdien til poengTeller med 1
    poengTeller += 1
    print(f"du fikk riktig")
# eller
else:
#     øk verdien til poengTellerMotsatt med 1
    poengTellerMotsatt +=1
    print("du fikk feil")
# print -----------------------------------
print("____________________________________")


# ta imot svar
svar5 = input(s5 + " ")
# hvis  input fra bruker er svar oslo
if svar5.lower() == "17":
#     øk verdien til poengTeller med 1
    poengTeller += 1
    print(f"du fikk riktig")
# eller
else:
#     øk verdien til poengTellerMotsatt med 1
    poengTellerMotsatt +=1
    print("du fikk feil")
# print -----------------------------------
print("____________________________________")


# ta imot svar
svar6 = input(s6 + " ")
# hvis  input fra bruker er svar oslo
if svar6.lower() == "ja":
#     øk verdien til poengTeller med 1
    poengTeller += 1
    print(f"du fikk riktig")
# eller
else:
#     øk verdien til poengTellerMotsatt med 1
    poengTellerMotsatt +=1
    print("du fikk feil")
# print -----------------------------------
print("____________________________________")


# ta imot svar
svar7 = input(s7 + " ")
# hvis  input fra bruker er svar oslo
if svar7.lower() == "ja":
#     øk verdien til poengTeller med 1
    poengTeller += 1
    print(f"du fikk riktig")
# eller
else:
#     øk verdien til poengTellerMotsatt med 1
    poengTellerMotsatt +=1
    print("du fikk feil")
# print -----------------------------------
print("____________________________________")


# ta imot svar
svar8 = input(s8 + " ")
# hvis  input fra bruker er svar oslo
if svar8.lower() == "ja":
#     øk verdien til poengTeller med 1
    poengTeller += 1
    print(f"du fikk riktig")
# eller
else:
#     øk verdien til poengTellerMotsatt med 1
    poengTellerMotsatt +=1
    print("du fikk feil")
# print -----------------------------------
print("____________________________________")


# ta imot svar
svar9 = input(s9 + " ")
# hvis  input fra bruker er svar oslo
if svar9.lower() == "ja":
#     øk verdien til poengTeller med 1
    poengTeller += 1
    print(f"du fikk riktig")
# eller
else:
#     øk verdien til poengTellerMotsatt med 1
    poengTellerMotsatt +=1
    print("du fikk feil")
# print -----------------------------------
print("____________________________________")


# ta imot svar
svar10 = input(s10 + " ")
# hvis  input fra bruker er svar oslo
if svar10.lower() == "ja":
#     øk verdien til poengTeller med 1
    poengTeller += 1
    print(f"du fikk riktig")
# eller
else:
#     øk verdien til poengTellerMotsatt med 1
    poengTellerMotsatt +=1
    print("du fikk feil")
# print -----------------------------------
print("____________________________________\n")

# print du fikk: {poengTeller} riktige
print(f"du fikk: {poengTeller} riktige.")
# print du fikk: {poengTellerMotsatt} feil
print(f"du fikk: {poengTellerMotsatt} feil.")

# print start programmet på nytt for å restarte...
print("\nstart programmet på nytt for å restarte...")


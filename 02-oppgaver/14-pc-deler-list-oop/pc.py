# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-07 11:09:18
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-12 18:47:18

# this is the super class for all the pc parts

# Opprett klassen Pc

    # Konstruktør med felles properties:
    # merke, modell, pris, inkjopspris, salgspris, tilstand
class Pc:
	def __init__(self, merke, modell, pris, inkjopspris, salgspris, tilstand):
		self.merke = merke
		self.modell = modell
		self.pris = pris
		self.inkjopspris = inkjopspris
		self.salgspris = salgspris
		self.tilstand = tilstand
 
	
  
  # funksjon for fortjeneste
  

    # Metode vis_komponent():
	def vis_komponent(self):
    # print merke
		print ("merke: ",self.merke)
    # print modell
		print ("modell: ",self.modell)
    # print pris
		print ("pris: ",self.pris)
    # print inkjopspris
		print ("inkjopspris: ",self.inkjopspris)
    # print salgspris
		print ("salgspris: ",self.salgspris)
    # print tilstand
		print ("tilstand: ",self.tilstand)

    # Metode fortjeneste():
	def fortjeneste(self):
		print(self.salgspris - self.inkjopspris)
    # regn ut salgspris - inkjopspris
    # print resultatet









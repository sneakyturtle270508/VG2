# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-12 18:40:53
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-12 18:44:03

from pc import Pc

class Ram(Pc):
    # Konstruktør - kall super og legg til egne properties:
	def __init__(self, merke, modell, pris, inkjopspris, salgspris, tilstand, kapasitet_gb, hastighet_mhz):
		super().__init__(merke, modell, pris, inkjopspris, salgspris, tilstand)
		self.kapasitet_gb = kapasitet_gb
		self.hastighet_mhz = hastighet_mhz
    # kapasitet_gb, hastighet_mhz
    # Override vis_komponent():
    # kall super sin vis_komponent()
	def vis_komponent(self):
		super().vis_komponent()
		print("kapasitet_gb",self.kapasitet_gb)
		print("hastighet",self.hastighet_mhz)
    # print kapasitet_gb
    # print hastighet_mhz

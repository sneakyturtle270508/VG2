# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-12 18:37:57
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-12 18:41:40
from pc import Pc

class Prosessor(Pc):
  
    # Konstruktør - kall super og legg til egne properties:
    # antall_kjerner, klokkefrekvens
  def __init__(self, merke, modell, pris, inkjopspris, salgspris, tilstand, antall_kjerner, klokkefrekvens):
    super().__init__(merke, modell, pris, inkjopspris, salgspris, tilstand)
    self.antall_kjerner = antall_kjerner
    self.klokkefrekvens = klokkefrekvens
    
  
    # Override vis_komponent():
  def vis_komponent(self):
    # kall super sin vis_komponent()
    super().vis_komponent()
    # print antall_kjerner
    print("antall_kjerner: ", self.antall_kjerner)
    # print klokkefrekvens
    print("klokkefrekvens: ", self.klokkefrekvens)
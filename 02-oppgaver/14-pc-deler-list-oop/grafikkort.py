# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-12 18:44:16
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-12 18:45:39
from pc import Pc

class Grafikkort(Pc):
    # Konstruktør - kall super og legg til egne properties:
    def __init__(self, merke, modell, pris, inkjopspris, salgspris, tilstand, vram_gb, minnetype):
     super().__init__(merke, modell, pris, inkjopspris, salgspris, tilstand)
    # vram_gb, minnetype
     self.vram_gb = vram_gb
     self.minnetype = minnetype
     
    def vis_komponent(self):
      super().vis_komponent()
      print("vram: ", self.vram_gb)
      print("minnetype: ", self.minnetype)

# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-07 08:59:37
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-07 10:31:28

from kjoretoy import Kjoretoy
# vi opretter klassen motorsykkel(mc):

class Bil(Kjoretoy):
  # opjekt-verdier:
  # construktor
  def __init__(self, merke, aarsmodell, farge, antall_dorer):
    super().__init__(merke, aarsmodell, farge)
    self.antall_dorer = antall_dorer
  def vis_data(self):
    super().vis_data()
    print("antall dører: ",self.antall_dorer)
	# her kommer objekt-metodene:









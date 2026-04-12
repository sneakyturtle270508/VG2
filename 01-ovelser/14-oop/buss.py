# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-07 08:59:37
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-07 10:47:45

from kjoretoy import Kjoretoy
# vi opretter klassen motorsykkel(mc):

class Buss(Kjoretoy):
  # opjekt-verdier:
  # construktor
  def __init__(self, merke, aarsmodell, farge, ant_seter):
    super().__init__(merke, aarsmodell, farge)
    self.ant_seter = ant_seter
  def vis_data(self):
    super().vis_data()
    print("antall seter: ",self.ant_seter)
	# her kommer objekt-metodene:









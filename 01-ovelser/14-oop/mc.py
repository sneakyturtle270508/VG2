# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-07 08:59:37
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-07 10:45:46

from kjoretoy import Kjoretoy
# vi opretter klassen motorsykkel(mc):

class Mc(Kjoretoy):
  # opjekt-verdier:
  # construktor
  def __init__(self, merke, aarsmodell, farge, drivverk):
    super().__init__(merke, aarsmodell, farge)
    self.drivverk = drivverk
  def vis_data(self):
    super().vis_data()
    print("drivverk",self.drivverk)
    # her kommer objekt-metodene:



# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-07 10:02:55
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-07 10:21:44



# vi oppretter klassen kjoretoy(super-klasse)

class Kjoretoy:
  # opjekt-verdier:
  # construktor
  def __init__(self, merke, aarsmodell, farge):
   self.merke = merke
   self.aarsmodell = aarsmodell
   self.farge = farge
  
  def vis_data(self):
    print("merke: ",self.merke)
    print("farge:",self.farge)
    print("årsmodell: ", self.aarsmodell)
    
	# her kommer objekt-metodene:
  def sett_farge(self, f):
    self.farge = f


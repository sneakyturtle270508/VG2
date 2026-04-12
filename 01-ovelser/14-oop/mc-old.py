# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-07 08:59:37
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-07 09:18:16


# vi opretter klassen motorsykkel(mc):

class Mc:
  # opjekt-verdier:
  merke = None
  aarsmodel = None
  farge = None
  drivverk = None
  def vis_data(self):
    print(self.merke),
    print(self.farge),
    print(self.aarsmodel),
    print(self.drivverk),
	# her kommer objekt-metodene:
  def sett_farge(self, f):
    self.farge = f


# oprett et objekt av klassen mc:
mc1 = Mc()
mc1.merke = "honda"
mc1.aarsmodel = "2021"
mc1.farge = "rød"
mc1.drivverk = "kjede"

mc2 = Mc()
mc2.merke = "kavasaki"
mc2.aarsmodel = "2003"
mc2.farge = "rød"
mc2.drivverk = "kjede"

mc3 = Mc()
mc3.merke = "harly-davidson"
mc3.aarsmodel = "1996"
mc3.farge = "sort"
mc3.drivverk = "reim"

mc4 = Mc()
mc4.merke = "bmw"
mc4.aarsmodel = "2017"
mc4.farge = "blå"
mc4.drivverk = "kardang"


# print objektet:
mc1.vis_data()
# endre farge på objektet:
print("------------------------")
mc1.sett_farge("grå")
mc1.vis_data()
print("------------------------")

# print objektet:
mc2.vis_data()
# endre farge på objektet:
print("------------------------")
mc2.sett_farge("grå")
mc2.vis_data()
print("------------------------")

# print objektet:
mc3.vis_data()
# endre farge på objektet:
print("------------------------")
mc3.sett_farge("grå")
mc3.vis_data()
print("------------------------")

# print objektet:
mc4.vis_data()
# endre farge på objektet:
print("------------------------")
mc4.sett_farge("grå")
mc4.vis_data()
print("------------------------")
# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-07 10:27:44
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-07 10:51:18


from bil import Bil
from mc import Mc
from buss import Buss
import os

os.system("cls")

print("mc1: ")
print("------------------")
mc1 = Mc("honda", "2021", "rød", "kjede")
mc1.vis_data()
print()

print("bil1: ")
print("------------------")
bil1 = Bil("opel", "2021", "rød", 3)
bil1.vis_data()
print()

print("buss1: ")
print("------------------")
buss1 = Buss("volvo", "2021", "gul", 50)
buss1.vis_data()
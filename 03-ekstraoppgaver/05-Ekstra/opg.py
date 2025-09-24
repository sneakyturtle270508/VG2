# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-09-21 18:52:35
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-21 19:05:50
import math

polsePrPakke = 10
brodPtPakke = 8

personer = int(input("hvor mange personer kommer: "))
prPosjon = int(input("hvor mange pølser pr posjon: "))

print(personer)
print(prPosjon)
antallPolser = personer * prPosjon

print(antallPolser)


antallPakkerPolser = math.ceil(antallPolser / polsePrPakke)

print(antallPakkerPolser)

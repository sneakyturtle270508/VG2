# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-09-23 08:16:46
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-23 08:29:03



# bruk av funsjoner 

def kvadrat(side):
    areal = side ** 2 # variabel er lokal / virker ikke på utsiden
    return areal

s = 3
print(kvadrat(s))

def rektangel(langside, kortside):
    nam = kortside * langside
    return nam

print(rektangel(3,6))

def rektangel_v2( kortside):
    langside = kortside * 2
    nam = kortside * langside
    return nam

print(rektangel_v2(5))

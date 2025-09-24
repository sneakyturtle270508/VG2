# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-09-23 08:37:16
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-23 09:00:54
import math



def kvadrat(s):
    a = s ** 2
    return a

def rektangel(g, h):
    a = g * h
    return a

def trekant(g, h):
    a = g * h / 2
    return a

def parallellogram(g, h):
    a = g * h
    return a

def rombe(g, h):
    a = g * h
    return a

def trapes(a , b , h):
    a = (a + b) * h / 2
    return a


def sirkel(r):
    a = math.pi * r ** 2
    d = 2 * r
    return a, d

print (kvadrat(9))
print (rektangel(6, 5))
print (trekant(3, 2))
print (parallellogram(6))
print (rombe(8))
print (trapes(4))
print (sirkel(2))


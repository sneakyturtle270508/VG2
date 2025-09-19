# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-08-24 19:23:34
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-08-24 19:38:49
var1 = 5 #integer pga heltal
print(type(var1))
var2 = 45.0 #float pga .000
print(type(var2))
var3 = 'text' #streng
print(type(var3))



# Apart from standard division (/), there is also floor division (//), 
# which is sometimes called integer division. How does it work? Given a // b
# it divides a by b, but always returns an integer value: any fractional part is 
# discarded. In other words, the result is always rounded down to the nearest integer. 
# For instance:
17/5 = 3.4
17//5 = 3

7/4 = 1.75
7//4 = 1


# Python also has a power operator: **. For instance:

number = 5
number_cubed = 5 ** 3
# 5 ** 3 means 'raise 5 to the third power', 
# so number_cubed will contain the value of

5*5*5 = 125.
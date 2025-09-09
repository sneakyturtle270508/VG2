# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-09-09 09:57:59
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-09 10:05:36

import time

antallRunder = int(input("hvor mange runder? "))

teller = 0

while teller != antallRunder:
    teller += 1
    print(teller)
    time.sleep(1)
    
print("du er ferdig")
# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-14 09:31:54
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-14 11:07:01
# !todo legg til roller og reset hver måne

from ansatt import Ansatt
from leder import Leder


ansatt1 = Ansatt(1, "william", "test", 160, 60)
ansatt2 = Ansatt(2, "sturle", "stiansen", 160, 60)
leder1 = Leder(1, "william", "berge", 150, 0.15, 150)

# ansatt1.endre_lonn(700)


alle_ansatte = [
    ansatt1,
    # ansatt2,
    # leder1,
]

for x in alle_ansatte:
    print("=" * 45)
    x.SkriveUt()
    x.beregn_lonn()
    x.regne_lonn_neste_12_m()

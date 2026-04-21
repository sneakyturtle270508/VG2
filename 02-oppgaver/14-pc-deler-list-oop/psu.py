# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-14 00:14:23
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-14 08:24:11

from pc import Pc


class Psu(Pc):
    def __init__(
        self,
        merke,
        modellnavn,
        inkjopspris,
        salgspris,
        tilstand,
        watt,
        effektivitet,
        modulaer_type,
        kabler,
        spenningsomraade,
        viftestorrelse_mm,
    ):
        super().__init__(merke, modellnavn, inkjopspris, salgspris, tilstand)
        self.watt = watt
        self.effektivitet = effektivitet
        self.modulaer_type = modulaer_type
        self.kabler = kabler
        self.spenningsomraade = spenningsomraade
        self.viftestorrelse_mm = viftestorrelse_mm

    def vis_komponent(self):
        print("PSU")
        super().vis_komponent()
        print(f"  watt:               {self.watt} W")
        print(f"  effektivitet:       {self.effektivitet}")
        print(f"  modulær_type:       {self.modulaer_type}")
        print(f"  kabler:             {self.kabler}")
        print(f"  spenningsområde:    {self.spenningsomraade}")
        print(f"  viftestørrelse:     {self.viftestorrelse_mm} mm")

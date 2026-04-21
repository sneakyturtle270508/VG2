# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-14 00:14:24
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-14 08:21:49

from pc import Pc


class Kjoeling(Pc):
    def __init__(
        self,
        merke,
        modellnavn,
        inkjopspris,
        salgspris,
        tilstand,
        kjoelingstype,
        viftestorrelse_mm,
        rpm,
        stoeynivaa_db,
        tdp_stoette_w,
        radiator,
    ):
        super().__init__(merke, modellnavn, inkjopspris, salgspris, tilstand)
        self.kjoelingstype = kjoelingstype
        self.viftestorrelse_mm = viftestorrelse_mm
        self.rpm = rpm
        self.stoeynivaa_db = stoeynivaa_db
        self.tdp_stoette_w = tdp_stoette_w
        self.radiator = radiator

    def vis_komponent(self):
        print("Kjøling")
        super().vis_komponent()
        print(f"  type:               {self.kjoelingstype}")
        print(f"  viftestørrelse:     {self.viftestorrelse_mm} mm")
        print(f"  RPM:                {self.rpm}")
        print(f"  støynivå:           {self.stoeynivaa_db} dB")
        print(f"  TDP_støtte:         {self.tdp_stoette_w} W")
        print(f"  radiator:           {self.radiator}")

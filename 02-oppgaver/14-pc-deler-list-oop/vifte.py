# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-14 00:14:35
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-14 08:25:04

from pc import Pc


class Vifte(Pc):
    def __init__(
        self,
        merke,
        modellnavn,
        inkjopspris,
        salgspris,
        tilstand,
        storrelse_mm,
        rpm,
        luftstroem_cfm,
        stoeynivaa_db,
        kontakt,
    ):
        super().__init__(merke, modellnavn, inkjopspris, salgspris, tilstand)
        self.storrelse_mm = storrelse_mm
        self.rpm = rpm
        self.luftstroem_cfm = luftstroem_cfm
        self.stoeynivaa_db = stoeynivaa_db
        self.kontakt = kontakt

    def vis_komponent(self):
        print("Vifte")
        super().vis_komponent()
        print(f"  størrelse:          {self.storrelse_mm} mm")
        print(f"  RPM:                {self.rpm}")
        print(f"  luftstrøm:          {self.luftstroem_cfm} CFM")
        print(f"  støynivå:           {self.stoeynivaa_db} dB")
        print(f"  kontakt:            {self.kontakt}")

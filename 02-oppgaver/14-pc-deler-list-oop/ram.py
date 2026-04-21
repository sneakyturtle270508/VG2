# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-14 00:14:15
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-14 08:24:23

from pc import Pc


class Ram(Pc):
    def __init__(
        self,
        merke,
        modellnavn,
        inkjopspris,
        salgspris,
        tilstand,
        kapasitet_gb,
        hastighet_mhz,
        type_ddr,
        latency_cl,
        antall_moduler,
        spenning_v,
        formfaktor,
    ):
        super().__init__(merke, modellnavn, inkjopspris, salgspris, tilstand)
        self.kapasitet_gb = kapasitet_gb
        self.hastighet_mhz = hastighet_mhz
        self.type_ddr = type_ddr
        self.latency_cl = latency_cl
        self.antall_moduler = antall_moduler
        self.spenning_v = spenning_v
        self.formfaktor = formfaktor

    def vis_komponent(self):
        print("RAM")
        super().vis_komponent()
        print(f"  kapasitet:          {self.kapasitet_gb} GB")
        print(f"  hastighet:          {self.hastighet_mhz} MHz")
        print(f"  type:               {self.type_ddr}")
        print(f"  latency:            CL{self.latency_cl}")
        print(f"  antall_moduler:     {self.antall_moduler}")
        print(f"  spenning:           {self.spenning_v} V")
        print(f"  formfaktor:         {self.formfaktor}")

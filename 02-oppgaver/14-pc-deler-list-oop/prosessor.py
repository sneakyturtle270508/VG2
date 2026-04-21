# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-14 00:13:55
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-14 08:24:00

from pc import Pc


class Prosessor(Pc):
    def __init__(
        self,
        merke,
        modellnavn,
        inkjopspris,
        salgspris,
        tilstand,
        antall_kjerner,
        antall_traader,
        basefrekvens,
        boostfrekvens,
        cache_mb,
        sokkeltype,
        tdp_w,
        integrert_grafikk,
    ):
        super().__init__(merke, modellnavn, inkjopspris, salgspris, tilstand)
        self.antall_kjerner = antall_kjerner
        self.antall_traader = antall_traader
        self.basefrekvens = basefrekvens
        self.boostfrekvens = boostfrekvens
        self.cache_mb = cache_mb
        self.sokkeltype = sokkeltype
        self.tdp_w = tdp_w
        self.integrert_grafikk = integrert_grafikk

    def vis_komponent(self):
        print("CPU")
        super().vis_komponent()
        print(f"  antall_kjerner:     {self.antall_kjerner}")
        print(f"  antall_tråder:      {self.antall_traader}")
        print(f"  basefrekvens:       {self.basefrekvens} GHz")
        print(f"  boostfrekvens:      {self.boostfrekvens} GHz")
        print(f"  cache:              {self.cache_mb} MB")
        print(f"  sokkeltype:         {self.sokkeltype}")
        print(f"  TDP:                {self.tdp_w} W")
        print(f"  integrert_grafikk:  {self.integrert_grafikk}")

# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-14 00:13:55
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-14 08:21:11

from pc import Pc


class Grafikkort(Pc):
    def __init__(
        self,
        merke,
        modellnavn,
        inkjopspris,
        salgspris,
        tilstand,
        vram_gb,
        vram_type,
        kjerner,
        klokkehastighet_mhz,
        stroemforbruk_w,
        utganger,
    ):
        super().__init__(merke, modellnavn, inkjopspris, salgspris, tilstand)
        self.vram_gb = vram_gb
        self.vram_type = vram_type
        self.kjerner = kjerner
        self.klokkehastighet_mhz = klokkehastighet_mhz
        self.stroemforbruk_w = stroemforbruk_w
        self.utganger = utganger

    def vis_komponent(self):
        print("GPU")
        super().vis_komponent()
        print(f"  VRAM:               {self.vram_gb} GB")
        print(f"  VRAM_type:          {self.vram_type}")
        print(f"  kjerner:            {self.kjerner}")
        print(f"  klokkehastighet:    {self.klokkehastighet_mhz} MHz")
        print(f"  strømforbruk:       {self.stroemforbruk_w} W")
        print(f"  utganger:           {self.utganger}")

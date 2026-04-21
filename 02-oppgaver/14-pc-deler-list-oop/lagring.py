# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-14 00:14:16
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-14 08:21:59

from pc import Pc


class Lagring(Pc):
    def __init__(
        self,
        merke,
        modellnavn,
        inkjopspris,
        salgspris,
        tilstand,
        kapasitet,
        lagringstype,
        grensesnitt,
        lesehastighet_mbs,
        skrivehastighet_mbs,
        formfaktor,
        cache_mb,
    ):
        super().__init__(merke, modellnavn, inkjopspris, salgspris, tilstand)
        self.kapasitet = kapasitet
        self.lagringstype = lagringstype
        self.grensesnitt = grensesnitt
        self.lesehastighet_mbs = lesehastighet_mbs
        self.skrivehastighet_mbs = skrivehastighet_mbs
        self.formfaktor = formfaktor
        self.cache_mb = cache_mb

    def vis_komponent(self):
        print("Lagring - SSD/HDD")
        super().vis_komponent()
        print(f"  kapasitet:          {self.kapasitet}")
        print(f"  type:               {self.lagringstype}")
        print(f"  grensesnitt:        {self.grensesnitt}")
        print(f"  lesehastighet:      {self.lesehastighet_mbs} MB/s")
        print(f"  skrivehastighet:    {self.skrivehastighet_mbs} MB/s")
        print(f"  formfaktor:         {self.formfaktor}")
        print(f"  cache:              {self.cache_mb} MB")

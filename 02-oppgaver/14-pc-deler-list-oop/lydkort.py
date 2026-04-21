# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-14 00:14:30
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-14 08:22:08

from pc import Pc


class Lydkort(Pc):
    def __init__(
        self,
        merke,
        modellnavn,
        inkjopspris,
        salgspris,
        tilstand,
        kanaler,
        samplingsrate_khz,
        grensesnitt,
    ):
        super().__init__(merke, modellnavn, inkjopspris, salgspris, tilstand)
        self.kanaler = kanaler
        self.samplingsrate_khz = samplingsrate_khz
        self.grensesnitt = grensesnitt

    def vis_komponent(self):
        print("Lydkort")
        super().vis_komponent()
        print(f"  kanaler:            {self.kanaler}")
        print(f"  samplingsrate:      {self.samplingsrate_khz} kHz")
        print(f"  grensesnitt:        {self.grensesnitt}")

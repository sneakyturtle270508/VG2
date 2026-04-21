# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-14 00:14:27
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-14 08:21:29

from pc import Pc


class Kabinett(Pc):
    def __init__(
        self,
        merke,
        modellnavn,
        inkjopspris,
        salgspris,
        tilstand,
        stoettede_formfaktorer,
        dimensjoner_mm,
        maks_gpu_lengde_mm,
        maks_cpu_kjoeler_hoyde_mm,
        vifteplasser,
        radiator_stoette,
        frontporter,
    ):
        super().__init__(merke, modellnavn, inkjopspris, salgspris, tilstand)
        self.stoettede_formfaktorer = stoettede_formfaktorer
        self.dimensjoner_mm = dimensjoner_mm
        self.maks_gpu_lengde_mm = maks_gpu_lengde_mm
        self.maks_cpu_kjoeler_hoyde_mm = maks_cpu_kjoeler_hoyde_mm
        self.vifteplasser = vifteplasser
        self.radiator_stoette = radiator_stoette
        self.frontporter = frontporter

    def vis_komponent(self):
        print("Kabinett")
        super().vis_komponent()
        print(f"  formfaktorer:       {self.stoettede_formfaktorer}")
        print(f"  dimensjoner:        {self.dimensjoner_mm} mm")
        print(f"  maks GPU-lengde:    {self.maks_gpu_lengde_mm} mm")
        print(f"  maks kjølerhøyde:   {self.maks_cpu_kjoeler_hoyde_mm} mm")
        print(f"  vifteplasser:       {self.vifteplasser}")
        print(f"  radiator_støtte:    {self.radiator_stoette}")
        print(f"  frontporter:        {self.frontporter}")

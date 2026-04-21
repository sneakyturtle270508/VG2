# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-14 00:16:07
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-14 08:22:16

from pc import Pc


class Nettverkskort(Pc):
    def __init__(
        self,
        merke,
        modellnavn,
        inkjopspris,
        salgspris,
        tilstand,
        nettverkstype,
        hastighet,
        wifi_standard,
        bluetooth_versjon,
    ):
        super().__init__(merke, modellnavn, inkjopspris, salgspris, tilstand)
        self.nettverkstype = nettverkstype
        self.hastighet = hastighet
        self.wifi_standard = wifi_standard
        self.bluetooth_versjon = bluetooth_versjon

    def vis_komponent(self):
        print("Nettverkskort / WiFi")
        super().vis_komponent()
        print(f"  type:               {self.nettverkstype}")
        print(f"  hastighet:          {self.hastighet}")
        print(f"  WiFi_standard:      {self.wifi_standard}")
        print(f"  Bluetooth:          {self.bluetooth_versjon}")

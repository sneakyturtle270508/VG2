# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-14 00:14:21
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-14 08:21:40

from pc import Pc


class Hovedkort(Pc):
    def __init__(
        self,
        merke,
        modellnavn,
        inkjopspris,
        salgspris,
        tilstand,
        sokkeltype,
        chipset,
        formfaktor,
        ram_slots,
        maks_ram_gb,
        pcie_slots,
        lagringsporter,
        usb_porter,
        bios_versjon,
    ):
        super().__init__(merke, modellnavn, inkjopspris, salgspris, tilstand)
        self.sokkeltype = sokkeltype
        self.chipset = chipset
        self.formfaktor = formfaktor
        self.ram_slots = ram_slots
        self.maks_ram_gb = maks_ram_gb
        self.pcie_slots = pcie_slots
        self.lagringsporter = lagringsporter
        self.usb_porter = usb_porter
        self.bios_versjon = bios_versjon

    def vis_komponent(self):
        print("Hovedkort")
        super().vis_komponent()
        print(f"  sokkeltype:         {self.sokkeltype}")
        print(f"  chipset:            {self.chipset}")
        print(f"  formfaktor:         {self.formfaktor}")
        print(f"  RAM_slots:          {self.ram_slots}")
        print(f"  maks_RAM:           {self.maks_ram_gb} GB")
        print(f"  PCIe_slots:         {self.pcie_slots}")
        print(f"  lagringsporter:     {self.lagringsporter}")
        print(f"  USB_porter:         {self.usb_porter}")
        print(f"  BIOS_versjon:       {self.bios_versjon}")

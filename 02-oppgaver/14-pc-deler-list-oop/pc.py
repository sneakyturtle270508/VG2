# -*- coding: utf-8 -*-
# Superklasse for alle PC-komponenter

class Pc:
    def __init__(self, merke, modellnavn, inkjopspris, salgspris, tilstand):
        self.merke = merke
        self.modellnavn = modellnavn
        self.inkjopspris = inkjopspris
        self.salgspris = salgspris
        self.tilstand = tilstand

    def vis_komponent(self):
        print(f"  merke:        {self.merke}")
        print(f"  modellnavn:   {self.modellnavn}")
        print(f"  inkjøpspris:  {self.inkjopspris} kr")
        print(f"  salgspris:    {self.salgspris} kr")
        print(f"  tilstand:     {self.tilstand}")

    def fortjeneste(self):
        return self.salgspris - self.inkjopspris

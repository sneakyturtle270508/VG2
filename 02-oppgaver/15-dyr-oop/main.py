# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-21 08:20:49
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-21 10:01:02



class Dyr:
    def __init__(self, navn, alder, art):
        self.navn = navn
        self.alder = alder
        self.art = art

  
    def presenter(self):
        print(
            f"jeg heter {self.navn}, jeg er en {self.art} og jeg er {self.alder} år gammel"
        )


    def bli_ett_aar_eldre(self):
        ny_alder = self.alder + 1
        print(f"etter ett år har jeg blitt {ny_alder} år gammel")
    def beskriv():
      print("")
					


# dyr1 = Dyr("test", 5, "hund")
# dyr2 = Dyr("burito", 2, "katt")

# dyr1.presenter()
# dyr1.bli_ett_aar_eldre()
# print("----------------")
# dyr2.presenter()
# dyr2.bli_ett_aar_eldre()



class Hund(Dyr):
	def __init__(self, navn, alder, art, rase):
		super().__init__(navn, alder, art)
		self.rase = rase

	def lag_lyd(self):
		print("voff")

	def hent(self):
		print("hunden hentet ballen!")

	def presenter(self):
		super().presenter()
	def beskriv(self):
		print( f"{self.navn} er en hund av rasen {self.rase}.")


class Katt(Dyr):

	def __init__(self, navn, alder, art, favorittmat):
		super().__init__(navn, alder, art)
		self.favorittmat = favorittmat

	def lag_lyd(self):
		print("Mjau")

	def klor(self):
		print("Katten klorer på sofaen!")
	def beskriv(self):
		print( f"{self.navn} og favorittmaten min er {self.favorittmat}.")


class Fugl(Dyr):
	def __init__(self, navn, alder, art, vingespenn):
		super().__init__(navn, alder, art)
		self.vingespenn = vingespenn
	def lag_lyd(self):
		print("pip,pip")
	def presenter(self):
		super().presenter()
		print(self.vingespenn)
	def beskriv(self):
		print( f"{self.navn} og vingespenne mitt er {self.vingespenn}.")

class Slange(Dyr):
	def __init__(self, navn, alder, art, giftig):
		super().__init__(navn, alder, art)
		self.giftig = giftig
	def lag_lyd(self):
		print("shshshshshshshshshs")
	def presenter(self):
		super().presenter()
		print(self.giftig)
	def beskriv(self):
		print( f"{self.navn}-slangen er {self.giftig}")


class Hest(Dyr):
	def __init__(self, navn, alder, art, vekt):
		super().__init__(navn, alder, art)
		self.vekt = vekt
	def lag_lyd(self):
		print("pyhyhyhyhyyhy")
	def presenter(self):
		super().presenter()
		print(self.vekt)
	def beskriv(self):
		print(f"{self.navn} er en hest som veier {self.vekt}")



class Fisk(Dyr):
	def __init__(self, navn, alder, art, farge):
		super().__init__(navn, alder, art)
		self.farge = farge
	def lag_lyd(self):
		print("blob,blob")
	def presenter(self):
		super().presenter()
		print(self.farge)
	def beskriv(self):
		print( f"{self.navn} er fargen {self.farge}.")



# dyr3 = Katt("sonja", 2, "katt", "burito eller taco")
# dyr3.presenter()
# dyr3.bli_ett_aar_eldre()
# dyr3.lag_lyd()
# print("----------")

# print("----------")
# dyr4 = Hund("kasper", 67, "hund", "sjefer")
# dyr4.presenter()
# dyr4.bli_ett_aar_eldre()
# dyr4.lag_lyd()

dyr1 = Hund("mari", 5, "hund", "chihuhu")
dyr2 = Katt("burito", 2, "katt", "taco")
dyr3 = Hest("middag", 3, "hest", "6 tonn")
dyr4 = Slange("Python", 3, "slange", "giftig")
dyr5 = Fisk("jens", 9, "fisk", "grønn")

alle_dyr = [
	dyr1,
	dyr2,
	dyr3,
	dyr4,
	dyr5,
]

for x in alle_dyr:
	print("-" * 45)
	x.presenter()
	x.beskriv()
	x.lag_lyd()
	x.bli_ett_aar_eldre()
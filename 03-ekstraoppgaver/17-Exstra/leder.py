# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-14 09:58:39
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-14 10:24:12

from person import Person


class Leder(Person):
	def __init__(self, person_id, fornavn, etternavn, timelonn, bunusandel, antall_timer):
		super().__init__(person_id, fornavn, etternavn, timelonn, antall_timer)
		self.bunusandel = bunusandel
  
	def beregn_lonn(self):
		baselonn = self.timelonn * self.antall_timer
		bonus = baselonn * self.bunusandel	
		
		print("lønn med bonus       ", bonus  + baselonn)
  
	def SkrivUt():
		super().SkriveUt()
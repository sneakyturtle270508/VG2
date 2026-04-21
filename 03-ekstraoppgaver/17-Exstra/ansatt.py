# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-14 09:19:56
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-14 10:26:40


from person import *

class Ansatt(Person):

	def __init__(self, person_id, fornavn, etternavn, timelonn, antall_timer):
		super().__init__(person_id, fornavn, etternavn, timelonn, antall_timer)

	def beregn_lonn(self):
		baselonn = self.timelonn * self.antall_timer
			
		print("måneslønn            ", baselonn)

	def endre_lonn(self, l):
		self.timelonn = l
   
	
	def SkriveUt(self):
		super().SkriveUt()









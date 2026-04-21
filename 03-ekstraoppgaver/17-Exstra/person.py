# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-14 08:43:31
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-14 12:16:40


class Person:

    def __init__(self, person_id, fornavn, etternavn, timelonn, antall_timer):
        self.person_id = person_id
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.timelonn = timelonn
        self.antall_timer = antall_timer

    def EndreLonn(self):
        print("test")

    def regne_lonn_neste_12_m(self):
        baselonn = self.antall_timer * self.timelonn
        maander = {
            "jan": baselonn,
            "feb": baselonn,
            "mar": baselonn,
            "apr": baselonn,
            "may": baselonn,
            "jun": baselonn + 3000000,
            "jul": baselonn,
            "aug": baselonn,
            "sep": baselonn,
            "oct": baselonn,
            "nov": baselonn,
            "dec": baselonn,
        }

        for maaned, lonn in maander.items():
            print("_" * 45)
            print(f"{maaned:<6} {lonn}")

    def SkriveUt(self):
        print("id:                  ", self.person_id)
        print("fornavn:             ", self.fornavn)
        print("etternavn:           ", self.etternavn)
        print("timeslønn:           ", self.timelonn)
        print("antall timer jobbet: ", self.antall_timer)

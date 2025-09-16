# # -*- coding: utf-8 -*-
# # @Author: William Berge Groensberg
# # @Date:   2025-09-16 08:22:42
# # @Last Modified by:   William Berge Groensberg
# # @Last Modified time: 2025-09-16 10:22:08



# teller = 300
# nevner = 100

# # divisjon
# # resultat = teller / nevner

# # print(resultat)

# # helltalsdivisjon
# resultat = teller // nevner

# print(resultat)

# # modulo

# resultat = teller % nevner

# print(resultat)





kjopePris = int(input("Hva er kjøpesummen: "))
# lag variabel betaltPris og giv input og mota svar om hvordan kunden vil betale
betaltPris = int(input("hva betaler du med "))



# lag variabel sjekkerIgjen og giv den verdi kjopePris % betaltPris
sjekkerIgjen = betaltPris % kjopePris

print(sjekkerIgjen)
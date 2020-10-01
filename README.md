# Gr4
# Bouchnafa Delsart Gaubil

from random import 


class Carte:


    def __init__(self, couleur = 0, valeur = 2):
        self.couleur = couleur
        self.valeur = valeur

    noms_couleurs = ['trèfle', 'carreau', 'cœur', 'pique']
    noms_valeurs = [None, 'as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D','R']

    def __str__(self):
        return '%s de %s' % (Carte.noms_valeurs[self.valeur],Carte.noms_couleurs[self.couleur])

        
class Croupier(Carte):
	
	def __init__(self):
		Carte.__init__()
		self.paquet = []
	def rassembler(self):
		for i in range(0, len(self.couleurs)):
			for j in range(0, len(self.valeur)):
				self.paquet.append(self.couleurs[i] + self.valeurs[j])

	def melanger(self): 
	

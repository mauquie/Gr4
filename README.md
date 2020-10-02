# Gr4
# Bouchnafa Delsart Gaubil

	from random import 


	class Carte:
	    #Représente une carte à jouer standard.

	    def __init__(self, couleur, valeur):
		self.couleur = couleur
		self.valeur = valeur
		
	class Joueur:
	  #Represente un joueur

	  def __init__(self, nom, main, tampis, combinaison):
	    self.nom=str(nom)
	    self.main=[]
	    self.tapis=int(tapis)
	    self.combinaison=combinaison

	  def evaluer(self):
	    pass


	  def nouvelle_donne(self):
	    pass


	  def recvoir_carte(self):
	    pass




	class Croupier(Carte):

		def __init__(self):
			Carte.__init__()
			self.paquet = []
		def rassembler(self):
			for i in range(0, len(self.couleurs)):
				for j in range(0, len(self.valeur)):
					self.paquet.append(self.couleurs[i] + self.valeurs[j])

		def melanger(self): 


# Gr4
# Bouchnafa Delsart Gaubil

	from random import 



	couleur=["carreau""coeur""pique""tréfle"]
	valeur=["2","3","4","5","6","7","8","9","10","valet","reine","roi","as"]
	t=1
	C=[]
	for i in range (couleur):
	  for j in range (rang):
	    C[t].append(carte(couleur[i],valeur[j]))
	    t=t+1

	joueur1=joueur(input("nom du joueur 1"))
	joueur.main=[C1,C2,C3,C4,C5]




	class Partie:

	  def __init__(self, joueurs):
	    self.list=joueur

	  def jouer(self):
	    pass
	    
	  
	class Carte:
	    #Représente une carte à jouer standard.

	    def __init__(self, couleur, valeur):
		self.couleur = couleur
		self.valeur = valeur
		
	class Joueur:
	  #Represente un joueur

	  def __init__(self, nom):
	    self.nom=str(nom)
	    self.main
	    self.tapis=1000
	    self.combinaison


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


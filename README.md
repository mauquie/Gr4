# Gr4
# Bouchnafa Delsart Gaubil

	from random import 


	couleur=["carreau""coeur""pique""tréfle"]
	valeur=["2","3","4","5","6","7","8","9","10","valet","reine","roi","as"]
	t=1
	C=[]
	for i in range (couleur):
	  for j in range (rang):
	    C[t].append(carte(couleur[i],valeur[k]))
	    t=t+1

	joueur1=joueur(input("nom du joueur 1"))
	joueur.main=[C1,C2,C3,C4,C5]


	class Coup:
	  #defini les coups
	    def __init__(croupier, gagnant, joueur):
	      self.croupier=Croupier
	      self.gagnant=Joueur
	      self.joueur=[]

	  def abattre(self):
	    pass


	  def distribuer(self):
	    pass

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
		
	class Joueur(Croupier):

	    def __init__(self , nom = "Joueur", main = None, tapis=1000):
		Croupier.__init__(self)
		self.nom=nom
		self.main=main#les cartes en main sont une liste
		self.tapis=tapis#tapis étant le nombre de jetons
		self.combinaison
		
	    def vider_main(self):
	    
		for i in range(0,5):#le mode de jeu est de 5 carte privatives...
		    self.main.pop()#on les supprimes

	    def recevoir(self):
	    
		if len(self.main + 1)!= 0:
		    vider_main()
		for i in range(5):
		    self.main.append(self.paquet[-1])
		    self.paquet.pop()
		    #besoin de 5 cartes

	class Croupier(Coup):

	    def __init__(self):
		Coup.__init__(self)
		self.paquet = []

	    def rassembler(self):
		for i in range(0, len(self.COULEURS)):
		    for k in range(0, len(self.VALEUR)):
			self.paquet.append(self.COULEURS[i] + self.VALEUR[k])

	    def melanger(self):
		random.shuffle(self.paquet)

	    def couper(self):
		rand = randint(1, 50)
		t_paquet = []
		for i in range (0, rand):
		    _paquett.append(self.paquet[0])
		    self.paquet.pop(0)
		for i in range (0, len(t_paquet)):
		    self.paquet.append(t_paquet[0])
		    t_paquet.pop(0)

	    def nouvelle_donne(self):
		self.rassembler()
		self.melanger()
		self.couper()



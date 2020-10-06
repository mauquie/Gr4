Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
from random import randint
class Joueur:

  def __init__(self, nom):
    self.nom=str(nom)
    self.main
    self.tapis=1000
    self.combinaison


  def vider_main(self):
      for i in range(0,5):
        self.main.pop()


  def evaluer(self):
    pass


  def nouvelle_donne(self):
    pass


  def recevoir_carte(self):
    if len(self.main) != 0 :
  		vider_main()
      for i in range(5):
      	self.main.append(self.paquet[-1])
      	self.paquet.pop()

class Partie:

  def __init__(self, joueurs):
    self.list=joueur

  def jouer(self):
    pass

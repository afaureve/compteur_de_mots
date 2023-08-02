from tkinter import *

class Compteur:
	"""compte les mots d'un d'un texte"""
	def __init__(self):
		self.window = Tk()

		self.window.title("Compteur")

		self.text = Text(self.window, height=40, width=100)
		self.text.grid(row=0, column=0, columnspan=3)
		
		self.bouton_compter = Button(self.window, text="Compter", command=self.compter)
		self.bouton_compter.grid(column=0, row=1)
		
		self.liste_mots = Text(self.window, height=40, width=30, state="disabled")
		self.liste_mots.grid(column=4, row=0)

		self.dico_mots = {}

		self.window.mainloop()

	def compter(self):
		self.liste_mots.config(state="normal")
		self.liste_mots.delete(1.0, END)
		self.dico_mots = {}
		liste_mots = self.text.get(1.0, END).split(" ")
		

		continuer = True
		while continuer:
			continuer = False
			liste_a_sup = []
			for i in range(len(liste_mots)):
				liste_mots[i] = liste_mots[i].lower()
				if len(liste_mots[i]) <= 1:
					liste_a_sup.append(i)
					continuer=True
				if len(liste_mots[i]) > 1 and liste_mots[i][-1] == "\n":
					liste_mots[i] = liste_mots[i][:-1]
					continuer=True
				if len(liste_mots[i]) > 1 and "\n" in liste_mots[i]:
					tmp = liste_mots[i].split("\n")
					for k in tmp:
						liste_mots.append(k)
					liste_a_sup.append(i)
					continuer=True
				if len(liste_mots[i]) > 2 and  liste_mots[i][1] == "'":
					liste_mots.append(liste_mots[i][:2])	
					liste_mots.append(liste_mots[i][2:])
					liste_a_sup.append(i)
					continuer=True
				if len(liste_mots[i]) > 3 and liste_mots[i][2] == "'":
					liste_mots.append(liste_mots[i][:3])	
					liste_mots.append(liste_mots[i][3:])
					liste_a_sup.append(i)
					continuer=True
				if len(liste_mots[i]) > 1 and liste_mots[i][-1] in [",", ".", ";", " "]:
					liste_mots[i] = liste_mots[i][:-1]
					continuer=True
			for i in liste_a_sup:
				del liste_mots[i]
				for k in range(len(liste_a_sup)):
					liste_a_sup[k] -= 1


		for i in liste_mots:
			try:
				self.dico_mots[i] += 1
			except KeyError:
				self.dico_mots[i] = 1
		
		liste_trie = []
		for i in self.dico_mots:
			liste_trie.append((self.dico_mots[i], i))
		liste_trie.sort()

		for i in liste_trie:
			self.liste_mots.insert(1.0, i[1]+": "+str(i[0])+"\n")
		
		nombre_mots = 0
		for i in liste_trie:
			nombre_mots += i[0]


		self.liste_mots.insert(1.0, "Liste des mots: \n")
		self.liste_mots.insert(1.0, "mots : "+str(nombre_mots)+"\n")
		
		self.liste_mots.config(state="disabled")



if __name__=="__main__":
	compteur = Compteur()

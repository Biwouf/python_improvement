#! /usr/bin/env python3.6
# coding: utf-8

import numpy as np
import pandas as pd 
import matplotlib as mpl 
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
import os

famille_panda = [
	[100, 5, 20, 80],
	[50, 2.5, 10, 40],
	[110, 6, 25, 90]
]

famille_panda_numpy = np.array(famille_panda)

#print(famille_panda_numpy[2,0])

famille_panda_df = pd.DataFrame(famille_panda_numpy, index = ['maman', 'bebe', 'papa'], columns = ['pattes', 'poils', 'queue', 'ventre'])
#print(famille_panda_df)
#print(famille_panda_df.ventre) 			#Imprime les mesures du ventre
#print(famille_panda_df['ventre'].values) 	#Imprime juste les valeurs

#iterrows() retourne un tuple avec (index, valeurs)
#for ligne in famille_panda_df.iterrows():
#	identity = ligne[0]
#	sizes = ligne[1]
#	print("Voici les mensurations de {}".format(identity))
#	print(sizes)
#	print("------------")

#print(famille_panda_df["pattes"] > 60)  	#Itère sur chaque index et pour chaque dis si c'est faux ou vrai

#Pour filtrer une partie du dataframe.
#Placer ~ devant le masque pour inverser le filtre > [~masque]
#masque = famille_panda_df["pattes"] > 60
#pandas_big_pattes = famille_panda_df[masque] 
#print(pandas_big_pattes)



mps = pd.read_csv("data/current_mps.csv", sep = ";")
#print(mps.iloc[0])
all_parties = mps["parti_ratt_financier"].dropna().unique()

#print(mps.nom[mps['parti_ratt_financier'] == 'En Marche !'])


class SetOfParliamentMembers:

	def __init__(self, name):
		self.name = name

	def data_from_csv(self, csv_file):
		self.dataframe = pd.read_csv(csv_file, sep= ";")

	def data_from_dataframe(self, dataframe):
		self.dataframe = dataframe

	def display_chart(self, party=''):
		data = self.dataframe
		females = data[data.sexe == 'F']
		males = data[data.sexe == 'H']

		counts = [len(females), len(males)]
		counts = np.array(counts)
		nb_mps = counts.sum()
		proportions = counts / nb_mps

		labels = ["Female ({})".format(counts[0]), "Male ({})".format(counts[1])]

		fig, ax = plt.subplots()
		ax.pie(proportions,
				labels=labels,
				autopct='%1.1f pourcents')
		ax.axis('equal')
		
		if party != '':
			plt.title('Répartition des sexes - {}'.format(party))
		else:
			plt.title('Répartition des sexes à l\'assemblée')

		plt.show()


	def split_by_political_party(self):
		result = {}
		data = self.dataframe

		all_parties = data["parti_ratt_financier"].dropna().unique()

		for party in all_parties:
			data_subset = data[data['parti_ratt_financier'] == party]			#Regroupe le dataframe complet pour ceux d'un même parti
			subset = SetOfParliamentMembers('MPs from party {}'.format(party))	#Création de l'objet avec le nom du parti en attribut
			subset.data_from_dataframe(data_subset)								#Insertion du dataframe dans l'objet
			result[party] = subset 												#Création d'un dico avec key > parti / value > sopm object

		return result

def launch_analysis(data_file, by_party=False):
	sopm = SetOfParliamentMembers('All MPS')
	data = sopm.data_from_csv(os.path.join("data", data_file))
	sopm.display_chart()

	if by_party:
		for party, s in sopm.split_by_political_party().items():
			s.display_chart(party)



def main():
	launch_analysis("current_mps.csv", False)

if __name__ == '__main__':
	main()


#Graph
#fig, ax = plt.subplots()
#ax.pie([24, 18], labels= ['Femmes', 'Hommes'],
#					autopct='%1.2f pourcents')		#Indique le nombre de chiffres après la virgule et la légende des unités
#ax.axis('equal')									#Pour un rendu plus beau
#plt.title("Répartition des sexes à l'assemblée")
#plt.show()


#! /usr/bin/env python3
# coding: utf-8

import os
import logging as lg

import numpy as np 
import pandas as pd
import matplotlib as mpl 
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

class SetOfParliamentMembers:

	def __init__(self, name):
		self.name = name

	def data_from_csv(self, csv_file):
		try:
			self.dataframe = pd.read_csv(csv_file, sep= ";")
		except FileNotFoundError as e:
			lg.critical('File not found ! Error {}'.format(e))


	def data_from_dataframe(self, dataframe):
		self.dataframe = dataframe

	def display_chart(self):
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
		plt.title('Répartition des sexes')
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
			s.display_chart()


def main():
	launch_analysis("current_mps.csv", True)

if __name__ == '__main__':
	main()


###### OLD ########
#lg.basicConfig(level=lg.DEBUG)

#def launch_analysis(data_file):
#	directory = os.path.dirname(os.path.dirname(__file__))
#	path_to_join = os.path.join(directory, 'data', data_file)
#	try:
#		with open(path_to_join, 'r') as file:
#			preview = file.readline()
#
#		lg.debug(preview)
#	except FileNotFoundError as e:
#		lg.critical('File not found ! Error : {}'.format(e))


#def main():
#	launch_analysis('current_mps.csv')

#if __name__ == "__main__":
#	main()
	
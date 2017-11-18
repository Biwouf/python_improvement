#! /usr/bin/env python3
# coding: utf-8

#Librairies
import argparse
import logging as lg
import re
from pathlib import Path

#Modules
import analysis.csv as c_an 
import analysis.xml as x_an

#Conf
lg.basicConfig(level=lg.DEBUG) 

#Main
def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-p", "--party", help="""Type the party for which you wanna know the parity. Spaces are handled""", nargs='+')			
	parser.add_argument("-a", "--all", help="""Say if you wanna browse all the parties""")
	parser.add_argument("-g", "--global", help="""Say if you just wanna see the global vision""", nargs='?', const=False)
	parser.add_argument("-i", "--info", help="""Info about the file""")
	parser.add_argument("-d", "--datafile", help="""Name of the datafile""")
	return parser.parse_args()

def main():
	args = parse_arguments()
	try:
		datafile = args.datafile
		if datafile == None:
			raise Warning('You must indicate a datafile')
	except Warning as e:
		lg.warning(e)
	else:
		if Path('data/', datafile).is_file():
			e = re.search('^.+\.(\D{3})', args.datafile)
			extension = e.group(1)

			if extension == 'csv':
				if args.party:
					c_an.launch_analysis(datafile, party=' '.join(args.party))
				elif args.all:
					c_an.launch_analysis(datafile, by_party=True)
				else:
					c_an.launch_analysis(datafile, view_all=True, info=args.info)
			elif extension == 'xml':
				lg.debug('Uncoded yet')
			else:
				lg.debug('Extension not managed')
		else:
			lg.critical('Either the file does not exist or it is not within the data directory')

if __name__ == "__main__":
	main()


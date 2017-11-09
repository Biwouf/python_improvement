#! /usr/bin/env python3
# coding: utf-8

#Librairies
import argparse
import logging as lg

#Modules
import analysis.csv as c_an 
import analysis.xml as x_an

#Conf
lg.basicConfig(level=lg.DEBUG) 

#Main
def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-e", '--extension', help="""Type of file to analyse. Is it XML or CSV?""")
	parser.add_argument("-p", "--party", help="""Type the party for which you wanna know the parity""")
	parser.add_argument("-a", "--all", help="""Say if you wanna browse all the parties""")
	parser.add_argument("-g", "--global", help="""Say if you just wanna see the global vision""", nargs='?', const=False)
	return parser.parse_args()

def main():
	args = parse_arguments()
	if args.party:
		c_an.launch_analysis("current_mps.csv", party=args.party)
	elif args.all:
		c_an.launch_analysis("current_mps.csv", by_party=True)
	else:
		lg.debug('Passed here')
		c_an.launch_analysis("current_mps.csv", view_all=True)

if __name__ == "__main__":
	main()


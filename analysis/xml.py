#! /usr/bin/env python3
# coding: utf-8

import os

def launch_analysis(data_file):
	directory = os.path.dirname(os.path.dirname(__file__))
	path_to_join = os.path.join(directory, 'data', data_file)
	with open(path_to_join, 'r') as file:
		preview = file.readline()

	print(preview)

def main():
	launch_analysis('SyceronBrut.xml')

if __name__ == "__main__":
	main()
	
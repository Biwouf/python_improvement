#! /usr/bin/env python3
# coding: utf-8

class MyIterator:

	def __init__(self):
		print("Je m'initialise à 40")
		self.i = 40

	def __iter__(self):
		print('On a appelé __iter__')
		return self

	def __next__(self):
		print('On appelé __next__')
		self.i += 2
		if self.i > 56:
			raise StopIteration()
		return self.i

def main():
	for i in MyIterator():
		print(i)


if __name__ == '__main__':
	main()
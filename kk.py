
from __future__ import print_function

import random
import sys

element = (
		("H",	"Hydrogen"),	# 1
		("He",	"Helium"),	# 2
		("Li",	"Lithium"),	# 3
		("Be",	"Beryllium"),	# 4
		("B",	"Boron"),	# 5
		("C",	"Carbon"),	# 6
		("N",	"Nitrogen"),	# 7
		("O",	"Oxygen"),	# 8
		("F",	"Flourine"),	# 9
		("Ne",	"Neon"),	# 10
		("Na",	"Sodium"),	# 11
		("Mg",	"Magnesium"),	# 12
		("Al",	"Aluminum"),	# 13
		("Si",	"Silicon"),	# 14
		("P",	"Phosphorus"),	# 15
		("S",	"Sulfur"),	# 16
		("Cl",	"Chlorine"),	# 17
		("Ar",	"Argon"),	# 18
		("K",	"Potassium"),	# 19
		("Ca",	"Calcium"),	# 20
		("Sc",	"Scandium"),	# 21
		("Ti",	"Titanium"),	# 22
		("V",	"Vandium"),	# 23
		("Cr",	"Chromium"),	# 24
		("Mn",	"Manganese"),	# 25
		("Fe",	"Iron"),	# 26
		("Co",	"Cobalt"),	# 27
		("Ni",	"Nickel"),	# 28
		("Cu",	"Copper"),	# 29
		("Zn",	"Zinc"),	# 30
		("Ga",	"Gallium"),	# 31
		("Ge",	"Germanium"),	# 32
		("As",	"Arsenic"),	# 33
		("Se",	"Selenium"),	# 34
		("Br",	"Bromine"),	# 35
		("Kr",	"Krypton"),	# 36
		("Rb",	"Rubidium"),	# 37
		("Sr",	"Strontium"),	# 38
		("Y",	"Yttrium"),	# 39
		("Zr",	"Zirconium"),	# 40
		)

class Element:
	def __init__(self, symbol, name, number, which):
		self.symbol = symbol
		self.name = name
		self.number = number
		self.which = which
		self.correct = False

	def get_ask(self):
		if self.which == 0:
			return self.symbol
		else:
			return self.name
	
	def get_answer(self):
		if self.which == 0:
			return self.name
		else:
			return self.symbol
	
	def mark_correct(self):
		self.correct = True


brain = list()

def setup():
	i = 1
	for e in element:
		brain.append(Element(e[0], e[1], i, 0))
		brain.append(Element(e[0], e[1], i, 1))

def main():
	setup()
	random.shuffle(brain)
	n = 0
	limit = len(brain)
	while len(brain) > 0:
		if n >= limit:
			random.shuffle(brain)
			limit = len(brain)
			n = 0
		e = brain.pop(0)
		n += 1

		question = ">> %s << ? " % e.get_ask()
		result = raw_input(question)

		if result.lower() != e.get_answer().lower():
			print("No, it was %s" % e.get_answer())
			brain.append(e)
		else:
			print("Right!")


if __name__ == "__main__":
	main()


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

def main():
	x = range(40)
	random.shuffle(x)
	for n in x:
		e = element[n]
		if random.random() < 0.5:
			ask = e[0]
			answer = e[1]
			query = "symbol"
			response = "name"
		else:
			ask = e[1]
			answer = e[0]
			query = "name"
			response = "symbol"

		result = raw_input("Element %s is %s; " \
		    "what is the element's %s? " % (query, ask, response))
		if result.lower() != answer.lower():
			print("No, it was %s" % answer)
		else:
			print("Right!")

if __name__ == "__main__":
	main()

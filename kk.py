
from __future__ import print_function

import random
import sys

from Tkinter import *

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


class Quiz:
	def __init__(self):
		self.brain = list()
		i = 1
		for e in element:
			self.brain.append(Element(e[0], e[1], i, 0))
			self.brain.append(Element(e[0], e[1], i, 1))
			i += 1
		random.shuffle(self.brain)
		self.n = 0
		self.limit = len(self.brain)

	def get_next(self):
		if len(self.brain) == 0:
			return None
		if self.n >= self.limit:
			random.shuffle(self.brain)
			limit = len(self.brain)
			self.n = 0
		self.n += 1
		return self.brain.pop(0)

	def re_ask(self, e):
		self.brain.append(e)

def ask():
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

class Window:
	def __init__(self):
		self.quiz = Quiz()
		self.cur = None

		self.root = Tk()
		self.frame = Frame(self.root)
		self.tl = Label(self.root, text="Questions left: %s" % \
                                len(self.quiz.brain), bg="light green",
                                font="Helvetica 16 bold")
		self.tl.pack(pady=5)
		self.query = Label(self.root, text=".",
                                   font="Helvetica 24 bold")
		self.query.pack(pady=15)
		self.response = Entry(self.root, justify=CENTER)
		self.response.pack(padx=20)
		self.startit = Button(self.frame,
				      text="Start!",
				      command=lambda: self.go(self))
		self.startit.pack(pady=30)
		self.frame.pack(padx=200, pady=100)
		self.root.bind("<Return>", self.check)

	def go(self, event):
		self.startit.pack_forget()
		self.cur = self.quiz.get_next()
                self.response.focus()
		self.query.config(text = self.cur.get_ask())

	def check(self, event):
		x = self.response.get()
		self.response.delete(0, END)
		if self.cur:
                        answer=self.cur.get_answer()
                        bg = "light green"
			if x.lower() != answer.lower():
				header = "No: %s is %s" % \
                                        (self.cur.get_ask(), answer)
                                bg="red2"
				self.quiz.re_ask(self.cur)
			else:
				qleft = len(self.quiz.brain)
				header = "Questions left: %s" % qleft
			self.cur = self.quiz.get_next()
			if not self.cur:
				self.startit.pack()
				self.tl.config(text="All done!")
				self.query.config(text=".")
				self.quiz = Quiz()
			else:
				self.query.config(text=self.cur.get_ask())
				self.tl.config(text=header, bg=bg)

	
	def run(self):
		self.root.mainloop()

def main():
	w = Window()
        try:
            w.run();
        except:
            print("Exiting.")

if __name__ == "__main__":
	main()

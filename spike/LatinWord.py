
from __future__ import print_function

import random
import sys

from Tkinter import *

element = (
		("aliquando", "sometimes"),	# 1
		("alius...alius", "one...another"),	# 2
		("alii...alii", "some...others"),	# 3
		("amplexus, amplexa, amplexum",	"having embraced"),	# 4
		("audacia, audaciae", "boldness, audacity"),	# 5
		("carmen, carminis", "song"),	# 6
		("circumvenio, circumvenire, circumveni", "surround"),	# 7
		("corona, coronae", "garland, wreath"),	# 8
		("cursus, cursus", "course, flight"),	# 9
		("defessus, defessa, defessum",	"exhausted, tired out"),	# 10
		("dolor, doloris", "grief, pain"),	# 11
		("ferrum, ferri", "iron, sword"),	# 12
		("incedo, incedere, incessi", "march, stride"),	# 13
		("liberi, liberorum",	"children"),	# 14
		("lux, lucis",	"light, daylight"),	# 15
		("malo, malle, malui",	"prefer"),	# 16
		("obscures, obscura, obscurum",	"dark, gloomy"),	# 17
		("odi",	"I hate"),	# 18
		("perficio, perficere, perfect", "finish"),	# 19
		("populus, populi", "people"),	# 20
		("prius", "earlier"),	# 21
		("quies, quietis", "rest"),	# 22
		("reduco, reducere, reduxi", "lead back"),	# 23
		("salus, salutis", "safety, health"),	# 24
		("scelus, sceleris", "crime"),	# 25
		("servo, servire, servivi", "serve"),	# 26
		("sors, sortis", "lot"),	# 27
		("sperno, spernere, sprevi", "despise, reject"),	# 28
		("undique", "on all sides"),	# 29
		("vester, vestra, vestrum",	"your"),	# 30
		("vivus, viva, vivum",	"alive, living"),	# 31
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
	
	def check_answer(self, answer):
		if self.which == 1:
			answers = self.symbol.split(", ")
		else:
			answers = self.name.split(", ")

		print("answer = %s; answers = %s" % (answer, answers))
		if answer in answers:
			return True

		return False


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
                        bg = "light green"
			if self.cur.check_answer(x.lower()):
				qleft = len(self.quiz.brain)
				header = "Questions left: %s" % qleft
			else:
				header = "No: %s is %s" % \
                                        (self.cur.get_ask(), self.cur.get_answer())
                                bg="red2"
				self.quiz.re_ask(self.cur)
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

'''
Created on Jul 1, 2018

@author: anish
'''
from random import randint
from collections import deque
class Card:
	def __init__(self, number):
		self.number = number   
	def faceup(self):
		print ( "[" + self.number + "]")
	def facedown(self):
		print ("[X]")
class Deck:
	def shuffle(self):
		for x in range(52):
			posa = randint(0,51)
			posb = randint(0,51)
			carriercard = self.deck[posa]
			self.deck[posa] = self.deck[posb]
			self.deck[posb] = carriercard	 
	def __init__(self):
		self.deck = deque([])
		DeckNumbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10","J", "Q", "K"]
		for x in range(4):
			for value in DeckNumbers:
				newcard = Card(value)
				self.deck.append(newcard)
		self.shuffle()
	def cards(self):
		for card in self.deck:
			print(card.number + ",")
	def draw(self, number, location):
		for x in range(number):
			location.append(self.deck.popleft())

'''
Created on Jul 1, 2018

@author: anish
'''
class Player:
	def __init__(self, cash):
		self.cash = cash
		self.hand = []
	def show(self):
		for card in self.hand:
			card.faceup()
		print("")
	def count(self):
		total = 0
		for card in self.hand:
			total += card.value()
		return total
class Dealer:
	def __init__(self):
		self.hand = []
	def show(self):#TODO: need to return something
		self.hand[0].faceup()
		self.hand[1].facedown()
		print("")
	def show_final(self): #TODO: need to return something
		for card in self.hand:
			card.faceup()
		print("")
	def count(self):
		total = 0
		for card in self.hand:
			total += card.value()
		return total
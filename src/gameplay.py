'''
Created on Jul 1, 2018

@author: anish
'''
from deck import Deck as Deck
import player as pl
def setup():
	global deck, player, dealer
	deck = Deck()
	player = pl.Player(1000)
	dealer = pl.Dealer()
def bet():
	global betAmount
	#print ("You have bet " + betAmount)
	betAmount = input("How much would you like to bet?")
	
def play():
	global player
	playType = ""
	while ((playType != "hit") or (playType != "stand")):  
		playType  = input("Would you like to hit, or stand").lower()
	if (playType == "hit"):
		deck.draw(1, player.hand)
		for card in player.hand:
			card.faceup()
	if (playType == "stand"): 
		return
def main():
	#setup
	setup()
	#loop
	print('Shuffling cards (1 deck)')
	gameLive = True
	while (gameLive == True):
		#dealer puts your cards
		print('Player Balance: ' + str(player.cash))
		betAmount = 0
		deck.draw(2,player.hand)
		for card in player.hand:
			card.faceup()
	#dealer puts their cards
		deck.draw(1, dealer.hand)
		card.faceup()	
		deck.draw(1, dealer.hand)
		card.facedown()
	#you bet
		bet()
	#you decide to get one more card
		play()
	#loop
	#dealer takes the cards as they add up to at least 17
main()
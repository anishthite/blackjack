'''
Created on Jul 1, 2018

@author: anish
'''
from deck import Deck as Deck
import player as pl

def setup():
	global deck, player, dealer, dealerWins, playerWins, draws
	deck = Deck()
	player = pl.Player(1000)
	dealer = pl.Dealer()
	dealerWins = 0
	playerWins = 0
	draws = 0
def bet():
	global betAmount
	#print ("You have bet " + betAmount)
	betAmount = input("How much would you like to bet?")
def score_hit():
	if (player.count() > 21):
		print ('Player Busted')
		dealer_wins()
		close()
		return	
	else:
		return
def play():
	global player, dealer
	playType = ""
	while ((playType != "hit") and (playType != "stand")):  
		playType  = input("Would you like to hit, or stand").lower()
	if (playType == "hit"):
		deck.draw(1, player.hand)
		dealer.show()
		player.show()
		score_hit()
		return True
	if (playType == "stand"): 
		return False
def player_wins():
	global playerWins, player
	player.cash += int(betAmount)
	playerWins +=1
def dealer_wins():
	global dealerWins, player
	player.cash -= int(betAmount)
	dealerWins +=1
def score():
	global dealerWins, playerWins, draws, player, dealer
	#player > 21
	if (player.count() > 21):
		print ('Player Busted')
		dealer_wins()
		return
	#dealer > 21
	elif (dealer.count() > 21):
		print ("Dealer Busted")
		player_wins()
		return
	#dealer > player
	elif (dealer.count() > player.count()):
		print ("Dealer more than Player")
		dealer_wins()
		return
	#player > dealer
	elif (player.count() > dealer.count()):
		print ("Player more than Dealer")
		player_wins()
		return	
	#deal = player
	else:
		print ("Draw")
		draws +=1
		return
def cover():
	global dealer, player
	while (dealer.count() < 17):
		deck.draw(1, dealer.hand)
	dealer.show_final()
	player.show()
#close if the cards <= 4
def close(): 
	global gameLive
	dealer.hand.clear()
	player.hand.clear()
	if len(deck.deck) <= 4:
		print ("Deck is complete")
		print ("PlayerWins: " + playerWins)
		print ("DealerWins: " + dealerWins)
		gameLive = False
		return	
	else: 
		return
def main():
	global deck, player, dealer, betAmount
	#setup
	setup()
	#loop
	print('Shuffling cards (1 deck)')
	gameLive = True
	while (gameLive == True):
		#dealer puts your cards
		print('Player Balance: ' + str(player.cash))
		betAmount = 0
	#dealer puts their cards
		deck.draw(2, dealer.hand)
		dealer.show()
		deck.draw(2,player.hand)
		player.show()
	#you bet
		bet()
	#you decide to get one more card
		continuePlay = True
		while (continuePlay == True):
			continuePlay = play()
	#dealer takes the cards as they add up to at least 17
		cover()
		score()
		close()
		
main()
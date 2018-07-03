'''
Created on Jul 1, 2018

@author: anish
'''
from deck import Deck as Deck
import player
global gameLive, deck, player
def setup():
    deck = Deck()
    player = player.Player(1000)
    dealer = player.Dealer()
    gameLive = True
def main():
    #setup
    setup()
    #loop
    print('Shuffling cards (1 deck)')
    print('Player Balance: ' + player.cash)
    while (gameLive == True):
        #dealer puts your cards
        deck.draw(2,player.hand)
     
    #dealer puts their cards
    #you bet
    #you decide to get one more card
    #loop
    #dealer takes the cards as they add up to at least 17
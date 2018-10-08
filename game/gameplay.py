'''
Created on Jul 1, 2018

author: anish
TODO: csv file, bot function, wrapper for people
'''
from deck import Deck as Deck
import player as pl
import enum
'''
GAME: creates instances of round, holds the init and closing methods

Round: 1 round of BJ, including multiple plays
'''

class Result(enum.Enum):
    """ Possible results for a round    """
    playerBusted = 0
    dealerBusted = 1
    dealerMore = 0
    playerMore = 1
    draw = 2
class PlayType(enum.Enum):
    """ Possible types of plays    """
    hit = 0
    stand = 1
class Round:
    """ One round of a Blackjack game, """
    def __init__(self,player,dealer,deck, gameType,betAmount):
        self.player = player
        self.dealer = dealer
        self.deck = deck
        self.gameType = gameType
        self.betAmount = betAmount
        #draw cards
        self.deck.draw(2, self.dealer.hand)
        self.dealer.show() 
        self.deck.draw(2, self.player.hand)
        self.player.show()
    def player_wins():
        global playerWins, player
        self.player.cash += self.betAmount
        playerWins +=1
    def dealer_wins():
        global dealerWins, player
        player.cash -= int(betAmount)
        dealerWins +=1
    def score_hit():
        if (self.player.count() > 21):
            dealer_wins()
            close()
            return Result.playerBusted	
        else:
            return None
    def score():
        playerCount = self.player.count()
        dealerCount = self.dealer.count()
        #player > 21
        if (playerCount > 21):
            dealer_wins()
            return Result.playerBusted
        #dealer > 21
        elif (dealerCount > 21):
            player_wins()
            return Result.dealerBusted
        #dealer > player
        elif (dealerCount > playerCount):
            dealer_wins()
            return Result.dealerMore
        #player > dealer
        elif (playerCount > dealerCount):
            player_wins()
            return Result.playerMore
        #deal = player
        else:
            draws +=1
            return result.draw
    def cover(self):
        while (self.dealer.count() < 17):
            self.deck.draw(1, self.dealer.hand)
        self.dealer.show_final()
        self.player.show()
    def play(self, playType):
        if (playType == PlayType.hit):
            self.deck.draw(1, self.player.hand)
            self.dealer.show()
            self.player.show()
            score_hit()
            return True
        if (playType == PlayType.stand): 
            return False
    def close():
        result = score()
        #TODO: finish implementing score in close 
        self.dealer.hand.clear()
        self.player.hand.clear()
        if len(self.deck.deck) <= 4:
            print ("Deck is complete")
            print ("PlayerWins: " + playerWins)
            print ("DealerWins: " + dealerWins)
        return

class Game:
    #return the 
    def __init__(self, startingAmount, gameType):
        self.deck = Deck()
        self.player = p1.Player(startingAmount)
        self.dealer - p1.Dealer()
        self.gameType = gameType
        self.dealer_wins = 0
        self.playerWins = 0
        self.draws = 0
        return startingAmount
    #TODO: def people wrapper
    #roundresult: oldaccount, betmoney, newaccount,  
    def round(self,betAmount): #TODO: find better name
        round = round(self.player, self.dealer,self.gameType,betAmount)
        gameLive = True
        roundresult.append()
        while (continuePlay == True):
            continuePlay = play.play()#TODO: playtype
        play.cover()
        play.close()
        return roundResult

def bot_play(playType):
        global player, dealer
    if (playType == "hit" or playType == "h"):
        deck.draw(1, player.hand)
        dealer.show()
        player.show()
        score_hit()
        return True
    if (playType == "stand" or playType == "s"): 
        return False
def player_play():
    global player, dealer
    playType = ""
    while (playType != "hit" and playType != "h" and playType != "stand" and playType != "s"):  
        playType  = input("Would you like to hit, or stand").lower()
    if (playType == "hit" or playType == "h"):
        deck.draw(1, player.hand)
        dealer.show()
        player.show()
        score_hit()
        return True
    if (playType == "stand" or playType == "s"): 
        return False


def main_method():
    global player, deck, dealer, betAmount
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
        playerplaying = True
        while (continuePlay == True and playerplaying == True):
            continuePlay = player_play()
    #dealer takes the cards as they add up to at least 17
        cover()
        score()
        close()
if __name__ == "__main__":
    main_method()
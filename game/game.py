from deck import Deck as Deck
import player as pl
import enum, uuid
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
class Game:
    """ One round of a Blackjack game, """
    def __init__(self, gameid, player, dealer,deck, gameType,betAmount):

        """ Creates the round, and draws 2 cards from the deck
            for the dealer, and 2 cards for the player. Also creates
            response to input in  csv"""
        self.response = []
        self.player = player
        self.dealer = dealer
        self.deck = deck
        self.gameType = gameType
        self.betAmount = betAmount
        self.id = uuid.uuid4()
        self.response.append(gameid, self.id, self.player.cash, betAmount)
        #draw cards
        self.deck.draw(2, self.dealer.hand)
        self.response.append(self.dealer.show())
        self.deck.draw(2, self.player.hand)
        self.response.append(self.player.show())
    def player_wins(self):
        global playerWins, player
        self.player.cash += self.betAmount
        playerWins +=1
    def dealer_wins(self):
        global dealerWins, player
        self.player.cash -= int(self.betAmount)
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
        while (self.dealer.count() < 16):
            self.deck.draw(1, self.dealer.hand)
        self.dealer.show_final()
        self.player.show()
    def display(self):
        return self.dealer.hand, self.player.hand
    def action(self, playType): #TODO: add dealer shown, playe shown, action
        if (playType == PlayType.hit):
            self.deck.draw(1, self.player.hand)
            self.reponse.append(self.dealer.show())
            self.response.append(self.player.show())
            score_hit()
            return True
        if (playType == PlayType.stand):
            return False
    def close(self,):
        result = score()
        #TODO: finish implementing score in close
        self.dealer.hand.clear()
        self.player.hand.clear()
        if len(self.deck.deck) <= 4:
            print ("Deck is complete")
            print ("PlayerWins: " + playerWins)
            print ("DealerWins: " + dealerWins)
        return

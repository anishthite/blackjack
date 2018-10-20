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

    def __init__(self, session_id, player, dealer,deck, gameType,betAmount):

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
        self.session_id = session_id

        #draw cards
        self.deck.draw(2, self.dealer.hand)
        self.deck.draw(2, self.player.hand)

    def response_init(self):
        self.response.clear()
        self.response.append(self.session_id, self.id, self.player.cash, self.betAmount)

    def display(self, final):
        if final:
            self.response.append(self.dealer.show_final(), self.dealer.count(), self.player.show(), self.player.count())
            return self.dealer.show_final(), self.player.show()
        else:
            self.response.append(self.dealer.show(), self.dealer.count(), self.player.show(), self.player.count())
            return self.dealer.show(), self.player.show()

    def action(self, playType):
        self.response.append(playType)
        if (playType == PlayType.hit):
            self.response.append(PlayType.name)
            self.deck.draw(1, self.player.hand)
            self.score_hit()
            return True
        if (playType == PlayType.stand):
            self.response.append(PlayType.name)
            self.cover()
            return False

    def score_hit(self):
        if (self.player.count() > 21):
            self.dealer_wins()
            self.close(Result.playerBusted)
        else:
            return None

    def score(self):
        playerCount = self.player.count()
        dealerCount = self.dealer.count()
        if (playerCount > 21):
            self.dealer_wins()
            self.close(Result.playerBusted)
        elif (dealerCount > 21):
            self.player_wins()
            self.close(Result.dealerBusted)
        elif (dealerCount > playerCount):
            self.dealer_wins()
            self.close(Result.dealerMore)
        elif (playerCount > dealerCount):
            self.player_wins()
            self.close(Result.playerMore)
        else:
            self.close(Result.draw)

    def cover(self):
        while (self.dealer.count() < 16):
            self.deck.draw(1, self.dealer.hand)
        self.display(True)
        self.score()

    def close(self, result):
        self.response.append(self.player.cash,result)
        self.dealer.hand.clear()
        self.player.hand.clear()

    def player_wins(self):
        global playerWins, player
        self.player.cash += self.betAmount

    def dealer_wins(self):
        global dealerWins, player
        self.player.cash -= int(self.betAmount)

from deck import Deck
import game
from bot import Bot

class Human(Bot):

    @classmethod
    def play(cls, output):
        human = Human(1000);
        while(True):
            blackjack = game.Game(human.id, human.player, human.dealer, Deck(), "human", Human.human_input_betAmount())
            roundContinue = True;
            while(roundContinue):
                blackjack.response_init()
                print(blackjack.display())
                roundContinue = blackjack.action(Human.human_input_action())
            Human.write_to_file(output, blackjack.response)

    @classmethod
    def human_input_betAmount(cls):
        betAmount = input("Bet Amount: ")
        return betAmount

    @classmethod
    def human_input_action(cls):
        action = input("Hit or Stand: ")
        if action.lower() == "hit" or action.lower() == "h":
            return game.PlayType.hit
        if action.lower() == "stand" or action.lower() == "s":
            return game.PlayType.stand
        return Human.human_input_action()


if __name__ == "__main__":
    Human.play("human.csv")
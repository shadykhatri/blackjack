#importing deck from deck.py
from deck import Deck
#importing player from player.py
from player import Player

#main class to run the code
class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.generate()
        self.player = Player(False, self.deck)
        self.dealer = Player(True, self.deck)

    def play(self):
        p_status = self.player.deal()
        d_status = self.dealer.deal()

        self.player.show()

        #if player scores 21, player wins
        if p_status == 1:
            print("Player got Blackjack! Congrats!")
            #if dealer also scores 21, it's a tie
            if d_status == 1:
                print("Dealer and Player got Blackjack! It's a push. (Tie)")
            return 1

        cmd = ""
        #keep running loop if Stand,stand not entered
        while cmd != "Stand" or "stand":
            bust = 0
            #taking user input to hit or stand
            cmd = input("Hit or Stand? ")

            #if Hit,hit entered, run hit and show function
            if cmd == "Hit" or "hit":
                bust = self.player.hit()
                self.player.show()
            #if score crosses 21, bust flag value will turn from 0 to 1 and player loses game
            if bust == 1:
                print("Player busted. Good Game!")
                return 1
        print("\n")
        self.dealer.show()
        if d_status == 1:
            print("Dealer got Blackjack! Better luck next time!")
            return 1
        #if dealer score is less than 17, add 1 more card and show cards, if score crosses 21 dealer loses
        while self.dealer.check_score() < 17:
            if self.dealer.hit() == 1:
                self.dealer.show()
                print("Dealer busted. Congrats!")
                return 1
            self.dealer.show()

        #compare dealer,player score, if equal, it's a tie
        if self.dealer.check_score() == self.player.check_score():
            print("It's a Push (Tie). Better luck next time!")
        #compare dealer,player score, if dealer score more, dealer wins
        elif self.dealer.check_score() > self.player.check_score():
            print("Dealer wins. Good Game!")
         #compare dealer,player score, if player score more, player wins
        elif self.dealer.check_score() < self.player.check_score():
            print("Player wins. Congratulations!")

b = Blackjack()
b.play()
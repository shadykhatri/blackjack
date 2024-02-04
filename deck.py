#importing python in build random module
import random
#importing card from card.py
from card import Card

#Deck class
class Deck:
    def __init__(self):
        #empty list of cards
        self.cards = []

    #generating cards and appending them to cards list
    def generate(self):
        for i in range(1, 14):
            for j in range(4):
                self.cards.append(Card(i, j))
    
    #function to draw cards, which appends, removes cards
    def draw(self, iteration):
        cards = []
        for i in range(iteration):
            card = random.choice(self.cards)
            self.cards.remove(card)
            cards.append(card)
        return cards

    def count(self):
        return len(self.cards)
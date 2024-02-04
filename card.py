#card class to create cards
class Card:
    def __init__(self,value,suit):
        self.cost = value
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][value-1]
        self.suit = '♥♦♣♠'[suit]
    
    #function to show cards on program run
    def show(self):
        print('┌───────┐')
        print(f'| {self.value:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.value:>2} |')
        print('└───────┘') 

    #function to display value of the cards
    def price(self):
        #card cost will be 10 if card value bigger than 10
        if self.cost >= 10:
            return 10
        #card value will be 11 if it is ace
        elif self.cost == 1:
            return 11
        return self.cost

    
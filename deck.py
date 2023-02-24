import card
import random

class Deck:
    def __init__(self):
        self.deck = []
        suits = ['spade', 'diamond', 'heart', 'club']
        denoms = list(range(2,15))
        for suit in suits:
            for denom in denoms:
                self.deck.append(card.Card(suit, denom))
                
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

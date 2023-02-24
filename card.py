class Card:
    def __init__(self, suit, denom):
        self.suit = suit
        self.denom = denom
        self.names = {
            11 : 'Jack',
            12 : 'Queen',
            13 : 'King', 
            14 : 'Ace'
        }
        for i in range(1, 11):
            self.names[i] = str(i)
            
    
    def view(self):
        return (self.suit, self.names[self.denom])

        
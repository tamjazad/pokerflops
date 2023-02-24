
import deck
import time

class Table:
    def __init__(self, num_hands):
        self.table = []
        self.hands = []
        self.mydeck = deck.Deck()
        self.mydeck.shuffle()
        self.deal_hands(num_hands)
        self.deal_table()
        
    def deal_hands(self, num_hands):
        for hand in range(num_hands):
            new_hand = []
            for i in range(2):
                new_hand.append(self.mydeck.deck.pop())
            self.hands.append(new_hand)
    
    def deal_table(self):
        self.deal_flop()
        self.deal_turn()
        self.deal_river()
    
    def deal_flop(self):
        for i in range(3):
            self.table.append(self.mydeck.deck.pop())
    
    def deal_turn(self):
        self.table.append(self.mydeck.deck.pop())
        
    def deal_river(self):
        self.table.append(self.mydeck.deck.pop())
        
    def view_table(self):
        return [ x.view() for x in self.table ]
    
    def view_hands(self):
        hand_dict = {}
        for i in range(len(self.hands)):
            hand_dict[i + 1] = [ x.view() for x in self.hands[i] ]
        
        return hand_dict

    def play_round(self):
        tableview = self.view_table()
        handview = self.view_hands()
        print("We're playing a {}-handed game!".format(len(self.hands)))
        time.sleep(0.5)
        print("*** THE HANDS ARE ***")
        for hand in handview:
            print(handview[hand])
            time.sleep(0.5)
        
        time.sleep(0.5)
        print("*** AND THE FLOP IS ***")
        time.sleep(1)
        for i in range(3):
            print(tableview[i])
            time.sleep(0.25)
        time.sleep(0.25)
        print("*** THE TURN IS ***")
        time.sleep(1)
        print(tableview[3])
        time.sleep(0.25)
        print("*** THE RIVER IS ***")
        time.sleep(1)
        print(tableview[4])
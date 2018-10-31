import random
suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen', 'King',]

class BlackJack:
    def __init__(self):
        self.used = []
        self.value = 0
        self.hand = [self.newCard() + self.newCard()]
        self.run()

    def run(self):
        while True:
            print('\nYour hand is valued at ' + str(self.value) + '.')
            hit = input('Hit or stay --> ')
            if hit == 'hit':
                self.hand.append(self.newCard())
                if self.value == 21:
                    print('Blackjack!')
                    break
                if self.value > 21:
                    print('Bust')
                    break
                    
            if hit == 'stay':
                print('Your final score is ' + str(self.value) + '.')
                break
        
    def newCard(self):
        while True:
            c = cards[random.randint(0, 11)]
            s = suits[random.randint(0,3)]
            card = c + ' of ' + s
            try:
                i = self.used.index(card)        
            except ValueError:
                self.used.append(card)
                print('Add ' + card + ' to your hand.')
                self.value += self.valueCard(c)
                break
        return card

    def valueCard(self, card):
        x = 0
        if card == 'Ace':
            j = input('Would you like this ace to be worth 1 or 11? --> ')
            return int(j)
        elif card == 'Jack' or card == 'Queen' or card == 'King':
            return 10
        else:
            return int(card)

temp = BlackJack()

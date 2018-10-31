#remove my hidden card from computer's used array

class Game:
    def __init__(self):
        self.suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        self.cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        #intitializes array of cards that have been played
        self.used = []
        self.rem = [1, 4, 8]
        #establish player's hand
        self.value = 0
        self.hand = [self.newCard(), self.newCard()]
        #establishes computer's hand
        self.cvalue = 0
        self.chand = [self.newCard(), self.newCard()]

        self.run()

    def run(self):
        print('Your visible card is ' + str(self.hand[0]))
        print('your opponents visible card is ' + str(self.chand[0]))
        
        while True:
            #your turn
            print('\nYour hand is valued at ' + str(self.value) + '.')
            hit = input('Hit or stay --> ')
            if hit == 'hit':
                self.hand.append(self.newCard('user'))
                if self.value == 21:
                    print('You hit Blackjack!')
                    break
                if self.value > 21:
                    print('You busted')
                    break
                    
            if hit == 'stay':
                print('Your final score is ' + str(self.value) + '.')
                break

            #computer's turn
            print("Computer's turn... ")
            dif = 21 - self.cvalue
            if dif >= 11:
                self.chand.append(self.newCard('computer'))
            prob = 

    def getChances(self):
        

            
    def choose(self):
        pass

    #adds a new card to player's hand 'user' for human 'computer' for computer
    def newCard(self, player):
        while True:
            c = cards[random.randint(0, 11)]
            s = suits[random.randint(0,3)]
            card = c + ' of ' + s
            try:
                i = self.used.index(card)        
            except ValueError:
                self.used.append(card)
                print('Add ' + card + ' to ' + player + "'s hand.")
                if player == 'user':
                    self.value += self.valueCard(c)
                if player == 'computer':
                    self.cvalue += self.valueCard(c)
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

'''
Author: Daniel Frederick
Date: October 30, 2018
--------------------------------------------------------------------------------------------------
Still need to add:
- remove user's hidden card from used array visible to Computer
- add support for ace to be 1 OR 11
- finish computer's turn
'''

#remove my hidden card from computer's used array
class Game:
    def __init__(self):
        self.suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        self.cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        #intitializes array of cards that have been played
        self.used = []
        self.rem = [4,4,4,4,4,4,4,4,16,4]
        #establish player's hand
        self.value = 0
        self.hand = [self.newCard(), self.newCard()]
        #establishes computer's hand
        self.cvalue = 0
        self.chand = [self.newCard(), self.newCard()]

        r = self.run()
        if r == 7:
            if self.value > self.cvalue:
                print('You were colser to 21. You win!')
                x = input('Press any key to exit --> ')
                exit()
            elif self.value < self.cvalue:
                print('The computer was closer to 21. You lose!')
                x = input('Press any key to exit --> ')
                exit()
        else:
            x = input('Press any key to exit --> ')
            exit()

    #returns 1 if you get blackjack, 2 if you lose
    # 5 if computer gets blackjack, and 6 if computer busts
    # 7 if you both stay
    def run(self):
        print('Your visible card is ' + str(self.hand[0]))
        print('your opponents visible card is ' + str(self.chand[0]))
        stay = False
        cstay = False
        while True:
            #your turn
            if stay == False:
                print('\nYour hand is valued at ' + str(self.value) + '.')
                hit = input('Hit or stay --> ')
                if hit == 'hit':
                    self.hand.append(self.newCard('user'))
                    if self.value == 21:
                        print('You hit Blackjack!')
                        return 1
                    if self.value > 21:
                        print('You busted. Computer wins!')
                        return 2

                if hit == 'stay':
                    print('Your final score is ' + str(self.value) + '.')
                    stay = True

            #computer's turn
                if cstay == False:
                    print("Computer's turn... ")
                    choice = self.choose()
                if choice == 'stay':
                    print('Computer chose to stay')
                    cstay = True
                if choice == 'hit':
                    self.chand.append(self.newCard('computer'))
                    if self.cvalue == 21:
                        print('Computer hit blackjack!')
                        return 5
                    if self.cvalue > 21:
                        print('Computer busted')
                        return 6

                if stay == False and cstay == False:
                    return 7


    #returns an array of percentage chance of drawing a card worth [2,3,4,5,6,7,8,9,10,11]
    def getChances(self):
        ans = []
        for i in range(0,9):
            ans.append(float(self.rem[i]) / float(52 - len(self.used))
        return ans

    def choose(self):
        dif = 21 - self.cvalue
        if dif >= 11:
            self.chand.append(self.newCard('computer'))
        prob = self.getChances()
        #chances of going over (drawing a card with a value larger than dif)
        bad = 0
        for i in range(int(dif),11):
            bad += prob(i)
        if bad > .5:
            return 'stay'
        else return 'hit'

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
            self.rem[10] = self.rem[10] - 1
            return int(j)
        elif card == 'Jack' or card == 'Queen' or card == 'King' or card == '10':
            self.rem[9] = self.rem[9] - 1
            return 10
        else:
            self.rem[int(card) - 2] = self.rem[int(card) - 2] - 1
            return int(card)

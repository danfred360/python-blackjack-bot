'''
Author: Daniel Frederick
Date: October 30, 2018
--------------------------------------------------------------------------------------------------
Still need to add:
- remove user's hidden card from used array visible to Computer
'''

import random


class Game:
    def __init__(self):
        self.suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        self.cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        # intitializes array of cards that have been played
        self.used = []
        #          [1,2,3,4,5,6,7,8,9,10,11]
        self.rem = [4, 4, 4, 4, 4, 4, 4, 4, 4, 16, 4]
        # establish player's hand
        self.value = 0
        self.hand = [self.newCard('user'), self.newCard('user')]
        # establishes computer's hand
        self.cvalue = 0
        self.chand = [self.newCard('computer'), self.newCard('computer', False)]
        # check to see if anyone one off the bat
        if self.value == 21:
            print('You hit blackjack!')
            x = input('\nPress any key to exit --> ')
            exit()
        if self.value > 21:
            print('You busted!')
            x = input('\nPress any key to exit --> ')
            exit()

        if self.cvalue == 21:
            print('Computer hit blackjack! You lose.')
            x = input('\nPress any key to exit --> ')
            exit()
        if self.cvalue > 21:
            print('Computer busted! You win.')
            x = input('\nPress any key to exit --> ')
            exit()

        r = self.run()
        if r == 7:
            if self.value > self.cvalue:
                print("The computer's score was " + self.cvalue + '.')
                print('You were closer to 21. You win!')
                x = input('\nPress any key to exit --> ')
                exit()
            elif self.value < self.cvalue:
                print("The computer's score was " + self.cvalue + '.')
                print('The computer was closer to 21. You lose!')
                x = input('\nPress any key to exit --> ')
                exit()
            elif self.value == self.cvalue:
                print("The computer's score was " + self.cvalue + '.')
                print('You tied!')
                x = input('\nPress any key to exit --> ')
                exit()
        else:
            x = input('\nPress any key to exit --> ')
            exit()

    # returns 1 if you get blackjack, 2 if you lose
    # 5 if computer gets blackjack, and 6 if computer busts
    # 7 if you both stay
    def run(self):
        print('\nYour visible card is ' + str(self.hand[0]))
        print('Your opponents visible card is ' + str(self.chand[0]))
        stay = False
        cstay = False
        while True:
            # your turn
            if not stay:
                print('\nYour turn... ')
                print('\nYour hand is valued at ' + str(self.value) + '.')
                hit = self.dec()
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

            # computer's turn
            if not cstay:
                print("\nComputer's turn... ")
                choice = self.choose()
                if choice == 'stay':
                    cstay = True
                if choice == 'hit':
                    self.chand.append(self.newCard('computer'))
                    if self.cvalue == 21:
                        print('Computer hit blackjack!')
                        return 5
                    if self.cvalue > 21:
                        print('Computer busted')
                        return 6

            if stay and cstay:
                return 7

    # gets player's decision to hit or stay, checks input
    def dec(self):
        while True:
            x = input("Hit or stay --> ")
            if x == 'hit' or x == 'stay':
                return x
            else:
                print('Sorry, try again.')


    # returns an array of percentage chance of drawing a card worth [2,3,4,5,6,7,8,9,10,11]
    def getChances(self):
        ans = []
        for i in range(0, 10):
            ans.append(float(self.rem[i]) / float(52 - len(self.used)))
        return ans

    def choose(self):
        dif = 21 - self.cvalue
        if dif >= 11:
            print('Computer hits.')
            return 'hit'
            # self.chand.append(self.newCard('computer'))
        prob = self.getChances()
        # chances of going over (drawing a card with a value larger than dif)
        bad = 0
        for i in range(int(dif), 10):
            bad += prob[i - 1]
        if bad > .5:
            print('Computer stays.')
            return 'stay'
        else:
            print('Computer hits.')
            return 'hit'

    # adds a new card to player's hand 'user' for human 'computer' for computer
    def newCard(self, player, p=True):
        while True:
            c = self.cards[random.randint(0, 11)]
            s = self.suits[random.randint(0, 3)]
            card = c + ' of ' + s
            try:
                i = self.used.index(card)
            except ValueError:
                self.used.append(card)
                if p:
                    print('Add ' + card + ' to ' + player + "'s hand.")
                if player == 'user':
                    self.value += self.valueCard(c)
                if player == 'computer':
                    self.cvalue += self.valueCard(c, player)
                break
        return card

    def valueCard(self, card, p='user'):
        x = 0
        if card == 'Ace':
            if p == 'user':
                while True:
                    j = input('Would you like this ace to be worth 1 or 11? --> ')
                    if j == '1' or j == '11':
                        break
                    else:
                        print('Sorry try again.')
                self.rem[10] = self.rem[9] - 1
                self.rem[0] = self.rem[0] - 1
                return int(j)
            if p == 'computer':
                dif = 21 - self.cvalue
                if dif >= 11:
                    self.rem[9] = self.rem[9] - 1
                    self.rem[0] = self.rem[0] - 1
                    return 11
                else:
                    self.rem[9] = self.rem[9] - 1
                    self.rem[0] = self.rem[0] - 1
                    return 1
        elif card == 'Jack' or card == 'Queen' or card == 'King' or card == '10':
            self.rem[8] = self.rem[8] - 1
            return 10
        else:
            self.rem[int(card) - 2] = self.rem[int(card) - 2] - 1
            return int(card)


temp = Game()

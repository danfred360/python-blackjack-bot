'''
Author: Daniel Frederick
Date: December 13, 2018
'''

import random

class card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.value = self.getValue()

    # gets value of card
    def getValue(self):
        pass


class game:
    def __init__(self):
        self.suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        self.cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        # array of used cards
        self.used = []

    # defines actions to be taken each turn
    def step(self):
        pass


class player:
    def __init__(self, name, t='p', g):
        self.name = name
        self.type = t
        # game player is a part of
        self.g = g
        # initillizes hand value
        self.value = 0
        # initializes hand
        self.hand = [self.newCard(), self.newCard()]

    # adds random card that hasn't been played yet to player's hand
    def newCard(self):
        while True:
            c = g.cards[random.randint(o, 11)]
            s = g.suits[random.randint(0, 3)]
            card = c + 'of' + s
            if c not in g.used:
                g.used.append(card)
                self.value += getValue(card)
                return card

    def getValue(self, card):
        

    # defines actions to be taken upon each turn
    def turn(self):
        pass


class gui:
    def __init__(self):
        pass
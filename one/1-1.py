# -*- coding:utf-8 -*-
# Author: your name
# Date: 2021-10-19 09:10:04
# LastEditTime: 2021-10-19 09:50:36
# LastEditors: Please set LastEditors
# Description: In User Settings Edit
# FilePath: /fluentpython/one/1.py
# 

"""
__len__
__getitem__
"""

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split(' ')

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        # print("##", position)
        return self._cards[position]


    def choice(self):
        return choice(self)


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    deck = FrenchDeck()
    # print(len(deck))
    # print(deck[0])
    # print(deck.choice())
    c = Card("Q", 'hearts')
    print(c in deck)

    
  
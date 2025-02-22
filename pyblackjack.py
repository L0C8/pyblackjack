from colorama import Fore, Back, Style
import os, random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Deck:
    def __init__(self):
        self.suites = ["Hearts", "Clubs", "Spades", "Diamonds"]
        self.symbols = ["♥", "♣", "♠", "♦"]
        self.ranks = ["Ace", "Two", "Three", "Four", "Five", "Six",
                      "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        self.value = [-1,2,3,4,5,6,7,8,9,10]
        self._build_deck()  
        self.shuffle()  

    def _build_deck(self):
        self.cards = []  # Clear existing deck
        for suite, symbol in zip(self.suites, self.symbols):
            for rank in self.ranks:
                if rank == "Ace":
                    value = -1
                elif rank in ["Jack", "Queen", "King"]:
                    value = 10
                else:
                    value = int(self.ranks.index(rank) + 1)
                self.cards.append(Card(value, rank, suite, symbol))

    def shuffle(self):
        """Shuffles the deck randomly."""
        random.shuffle(self.cards)

    def draw_card(self):
        """Draws a card from the deck."""
        if len(self.cards) == 0:
            print("Deck is empty, reshuffling...")
            self._build_deck()
            self.shuffle()
        return self.cards.pop()

class Card:
    def __init__(self, value, rank, suite, symbol):
        self.value = value
        self.rank = rank
        self.suite = suite
        self.symbol = symbol
    
    def __str__(self):
        return f"{self.rank} of {self.suite} {self.symbol} (Value: {self.value})"
    
class Game:
    score = 0
    
    def __init__(self, start):
        self.score = start
    
    def addScore(self, val):
        self.score += val 
    
    def getScore(self):
        return self.score 
    
deck = Deck()
print(deck.draw_card())
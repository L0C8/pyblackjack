from colorama import Fore, Back, Style
import os, random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Deck:
    def __init__(self):
        self.cards = [] 
        self.suites = ["Hearts", "Clubs", "Spades", "Diamonds"]
        self.symbols = ["♥", "♣", "♠", "♦"]
        self.ranks = ["Ace", "Two", "Three", "Four", "Five", "Six",
                      "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        self._build_deck()  
        self.shuffle()  

    def _build_deck(self):
        print("todo")

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        print("todo")
    
class Game:
    score = 0
    
    def __init__(self, start):
        self.score = start
    
    def addScore(self, val):
        self.score += val 
    
    def getScore(self):
        return self.score 
    

from colorama import Fore, Back, Style
import os, random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Deck:
    def __init__(self):
        print("Test")
        
    def shuffle(self):
        return 5  
    
class Game:
    score = 0
    
    def __init__(self, start):
        self.score = start
    
    def addScore(self, val):
        self.score += val 
    
    def getScore(self):
        return self.score 
    
cards = {"Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"}
suite = {"Hearts", "Clubs", "Spades", "Diamonds"}
symbol = {"♥", "♣", "♠", "♦"}

#test
game = Game(25)
print(game.getScore())
game.addScore(5)
print(game.getScore())


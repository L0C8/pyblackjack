from colorama import Fore, Style
import os
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Deck:
    def __init__(self):
        self.suites = ["Hearts", "Clubs", "Spades", "Diamonds"]
        self.symbols = ["♥", "♣", "♠", "♦"]
        self.ranks = ["Ace", "Two", "Three", "Four", "Five", "Six",
                      "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        self.cards = []
        self._build_deck()
        self.shuffle()

    def _build_deck(self):
        self.cards = []
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
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) == 0:
            self._build_deck()
            self.shuffle()
        return self.cards.pop()

    def cards_left(self):
        return len(self.cards)


class Card:
    def __init__(self, value, rank, suite, symbol):
        self.value = value
        self.rank = rank
        self.suite = suite
        self.symbol = symbol

    def __str__(self):
        return f"{self.rank} of {self.suite} {self.symbol}"

    def get_value(self, current_total):
        """Handles Ace as 1 or 11 dynamically."""
        if self.value == -1:
            return 11 if current_total + 11 <= 21 else 1
        return self.value


class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = []
        self.dealer_hand = []
        self.player_score = 0
        self.dealer_score = 0

    def start_game(self):
        clear()
        print(Fore.GREEN + "Welcome to Terminal Blackjack!\n" + Style.RESET_ALL)

        for _ in range(2):
            self.player_hand.append(self.deck.draw_card())
            self.dealer_hand.append(self.deck.draw_card())

        self.show_hands(initial=True)

        self.player_turn()

        if self.calculate_hand_value(self.player_hand) <= 21:
            self.dealer_turn()

        self.determine_winner()

    def player_turn(self):
        while True:
            choice = input("Do you want to (H)it or (S)tand? ").lower()
            if choice == 'h':
                card = self.deck.draw_card()
                self.player_hand.append(card)
                print(f"\nYou drew: {card}")
                self.show_hands(initial=True)

                if self.calculate_hand_value(self.player_hand) > 21:
                    print(Fore.RED + "Bust! You exceeded 21." + Style.RESET_ALL)
                    break
            elif choice == 's':
                print("You chose to stand.\n")
                break
            else:
                print("Invalid choice. Please choose H or S.")

    def dealer_turn(self):
        print(Fore.YELLOW + "Dealer's turn..." + Style.RESET_ALL)
        self.show_hands(initial=False)

        while self.calculate_hand_value(self.dealer_hand) < 17:
            card = self.deck.draw_card()
            self.dealer_hand.append(card)
            print(f"Dealer drew: {card}")
            self.show_hands(initial=False)

    def calculate_hand_value(self, hand):
        total = 0
        for card in hand:
            total += card.get_value(total)
        return total

    def show_hands(self, initial):
        print("\nYour hand:")
        for card in self.player_hand:
            print(f" - {card}")
        print(f"Total value: {self.calculate_hand_value(self.player_hand)}")

        print("\nDealer's hand:")
        if initial:
            print(f" - {self.dealer_hand[0]}")  
            print(" - Hidden Card")
        else:
            for card in self.dealer_hand:
                print(f" - {card}")
            print(f"Total value: {self.calculate_hand_value(self.dealer_hand)}")
        print()

    def determine_winner(self):
        player_total = self.calculate_hand_value(self.player_hand)
        dealer_total = self.calculate_hand_value(self.dealer_hand)

        print(Fore.CYAN + "\n--- Final Results ---" + Style.RESET_ALL)
        print(f"Your total: {player_total}")
        print(f"Dealer's total: {dealer_total}")

        if player_total > 21:
            print(Fore.RED + "You busted! Dealer wins." + Style.RESET_ALL)
        elif dealer_total > 21:
            print(Fore.GREEN + "Dealer busted! You win!" + Style.RESET_ALL)
        elif player_total > dealer_total:
            print(Fore.GREEN + "You win!" + Style.RESET_ALL)
        elif player_total < dealer_total:
            print(Fore.RED + "Dealer wins!" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "It's a tie!" + Style.RESET_ALL)

if __name__ == "__main__":
    game = BlackjackGame()
    while True:
        game.start_game()
        again = input("Play again? (Y/N): ").lower()
        if again != 'y':
            break
        game = BlackjackGame()
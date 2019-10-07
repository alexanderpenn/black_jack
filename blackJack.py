#!/usr/bin/python
import random


class Game:
    def __init__(self):
        self.dealer = None
        self.player = None

        self.start_new_game()
        self.play_game()

    def start_new_game(self):
        print("Welcome to Alexander's Black Jack Game. I wish you the best of luck!")
        self.player = Player()
        self.dealer = Dealer()

    def play_game(self):
        stay = True
        while stay:
            self.play_hand()
            self.player.hand = []
            self.dealer.hand = []
            if self.player.capital <= 0:
                print("You gambled away all of your money ")
                break
            if len(self.dealer.deck.cards) <= 15:
                print("Congratulations! You have exhausted the deck and won. Your earned ${}".format(
                    self.player.capital))
                break

            stay = self.proposition_to_play_next_hand()

    def play_hand(self):
        player = self.player
        dealer = self.dealer

        bet = player.place_bet()
        dealer.deal(player)
        player_bust = player.make_decision(dealer)

        if player_bust == "Bust":
            print("You busted.")
            return

        dealer_bust = dealer.make_decisions()

        if dealer_bust == "Bust":
            player.capital += bet * 2
            print("The dealer busts You win ${} this hand!".format(bet * 2))
            return

        self.identify_winner(bet)

    @staticmethod
    def proposition_to_play_next_hand():
        truth_map = {"Y": True, "N": False}
        leave = input("Would you like to continue playing? (Y/N): ")
        while leave != "Y" and leave != "N":
            print("Invalid input. Please enter \"Y\" or \"N\".")
            leave = input("Would you like to play another game? (Y/N): ")

        return truth_map[leave]

    def check_for_naturals(self):
        player = self.player
        dealer = self.dealer

        if player.has_blackjack() and dealer.has_blackjack():
            pass
        elif player.has_blackjack() and not dealer.has_blackjack():
            pass
        elif not player.has_blackjack() and dealer.has_blackjack():
            pass
        else:
            pass

    def identify_winner(self, bet):
        player = self.player
        dealer = self.dealer

        if player.total_hand() > dealer.total_hand():
            player.capital += bet * 2
            print("You beat the dealer\'s {} with {}. You win ${}.".format(dealer.total_hand(), player.total_hand(),
                                                                           bet * 2))

        elif player.total_hand() < dealer.total_hand():
            print("You lost to the dealer\'s {} with {}".format(dealer.total_hand(), player.total_hand()))
        else:
            player.capital += bet
            print("You and the dealer both had {}. You push and get back your bet of {}.".format(player.reveal_cards,
                                                                                                 bet))


class Person:

    def receive_card(self, card):
        self.hand.append(card)

    def total_hand(self):
        for card in self.hand:
            if card == "Ace":
                self.hand.remove(card)
                self.hand.append(card)
        remaining_cards = len(self.hand)

        total = 0
        for card in self.hand:
            if not type(card) == int and card != "Ace":
                total += 10
            elif card == "Ace" and total <= (11 - remaining_cards):
                total += 11
            elif card == "Ace":
                total += 1
            else:
                total += card
            remaining_cards -= 1
        return total

    def has_blackjack(self):
        return self.total_hand() == 21


class Player(Person):

    def __init__(self):
        self.capital = 100
        self.hand = []

    def place_bet(self):
        bet = input("You have ${}. What would you like to bet? (Enter an integer): ".format(self.capital))

        while not bet.isdigit() or int(bet) > self.capital or int(bet) <= 0:
            print("Invalid input.")
            bet = input("You have ${} . What would you like to bet? (Enter an integer): ".format(self.capital))

        self.capital -= int(bet)
        return int(bet)

    def make_decision(self, dealer):
        decision = input("Would you like to stand or hit (Stand / Hit): ")

        while decision != "Stand" and decision != "Hit":
            print('Invalid input')
            decision = input("Would you like to stand or hit (Stand / Hit): ")

        while decision == "Hit":
            card = dealer.hit()
            self.hand.append(card)
            print("You were dealt a {}.".format(card))
            if self.total_hand() > 21:
                return 'Bust'

            decision = input("Would you like to stand or hit (Stand / Hit): ")
            while decision != "Stand" and decision != "Hit":
                print('Invalid input')
                decision = input("Would you like to stand or hit (Stand / Hit): ")


class Dealer(Person):

    def __init__(self):
        self.deck = Deck()
        self.hand = []

    def deal(self, player):
        deck = self.deck
        deck.shuffle_deck()
        player_card = deck.hit()
        dealer_card = deck.hit()

        player.receive_card(player_card)
        self.receive_card(dealer_card)

        print("You received a {}.".format(player_card))
        print("The dealer received a {}.".format(dealer_card))

        player_card = deck.hit()
        dealer_card = deck.hit()

        player.receive_card(player_card)
        self.receive_card(dealer_card)

        print("You received a {}.".format(player_card))

    def hit(self):
        return self.deck.hit()

    def make_decisions(self):
        while self.total_hand() < 17:
            card = self.hit()
            self.hand.append(card)
            print("The dealer drew a {}.".format(card))
            if self.total_hand() > 21:
                return "Bust"


class Deck:
    def __init__(self):
        self.cards = None
        self.build_deck()

    def build_deck(self):
        face_cards = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace", }
        cards = [value for _ in range(12) for value in range(2, 15)]

        cards = [face_cards[card] if card in face_cards else card for card in cards]
        self.cards = cards

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def hit(self):
        return self.cards.pop()


if __name__ == "__main__":
    Game()

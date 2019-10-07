# Black Jack

How To Run The Card Game:
1. Download the file blackJack.py
2. In the command line enter ./blackJack.py and then hit enter.


Design Choices:
Given the limited scope of this applciation, I felt the most interesting design choice I amde was to use object oriented programming to represent the game state, player, dealer, and deck of cards. I went with this choice in order to increase both modularity and scalability, such that I can model the interactions among elements in a manner which will facilate easier future development

I chose to make the end conditions of the game either exhausting the deck, which consisted of getting the deck beneath 15 cards (I used three decks in the game ot ensure that this would take time), choosing to leave, or of course running out of money.

To keep this simple, I built everything in Python, and only used the random library, which served the purpose of shuffling the deck.

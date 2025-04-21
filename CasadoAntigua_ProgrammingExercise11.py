import random

class Deck():

    def __init__(self, n_decks=1):
        self.card_list = [num + suit
                          for suit in '\u2665\u2666\u2663\u2660'
                          for num in 'A23456789TJQK'
                          for deck in range (n_decks)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)


    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print('Reshuffling...')
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)

        return new_card

    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()


def discard(card_hand, cards_to_discard, deck):
    for item in cards_to_discard:
        card_hand.pop(item - 1)
        card_hand.append(deck.deal())

    return card_hand


def main():
    # init list to use index to deal with specific slots
    hand = []
    discard_list = []

    print('Poker hand time')

    dk = Deck(1) # 1 deck instead of the 6 deck shoe thing


    for i in range(5):
        hand.append(dk.deal())
        print(dk.deal(), end = '  ')

    loop_rep = input('\nHow many cards would you like to discard? (0-5) ')

    try:
        loop_rep = int(loop_rep)
    except ValueError:
        print('Error: Invalid Input')

    if loop_rep > 5:
        print('Error: Discarding more cards than in hand')
    elif loop_rep < 0:
        print('Error: Discarding a negative amount')
    elif loop_rep == 0:
            print('Thanks for playing')

    for i in range(loop_rep):
        discard_pos = int(input('Which card would you like to discard? (input position 1-5) '))

        discard_list.append(discard_pos)

    hand = discard(hand, discard_list, dk)

    print(*hand, end='  ')










main()
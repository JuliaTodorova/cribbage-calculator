class Hand:

    def __init__(self, cards, values, suit, player):

        self._cards = cards
        self._values = values
        self._suit = suit
        self._player = player

    def get_cards(self):
        return self._cards

    def set_cards(self, cards):
        self._cards = cards

    def get_values(self):
        return self._values

    def set_values(self, values):
        self._values = values

    def get_suit(self):
        return self._suit

    def set_suit(self, suit):
        self._suit = suit

    def get_player(self):
        return self._player

    def set_player(self, player):
        self._player = player

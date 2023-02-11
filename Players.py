class Players:

    def __init__(self,
                 player,
                 cards,
                 crib,
                 score
                 ):
        self._player = player
        self._cards = cards
        self._crib = crib
        self._score = score


    def get_score(self):
        return self._score

    def set_score(self, score):
        self._score = score

    def get_crib(self):
        return self._crib

    def set_crib(self, crib):
        self._crib = crib

    def get_cards(self):
        return self._cards

    def set_cards(self, cards):
        self._cards = cards

    def get_suit(self):
        return self._suit

    def set_suit(self, suit):
        self._suit = suit

    def get_player(self):
        return self._player

    def set_player(self, player):
        self._player = player

    def print_player(self):
        return f" score {self._score}, " \
               f"player {self._player}," \
               f"crib {self._crib},"\
               f"cards {self._cards}"

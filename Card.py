class Card:

    def __init__(self,
                 value,
                 suit
                 ):
        self._value = value
        self._suit = suit

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def get_suit(self):
        return self._suit

    def set_suit(self, suit):
        self._value = suit

    def print_card(self):
        return f" value {self._value}, " \
               f" suit {self._suit}, "


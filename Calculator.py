
class Calculator:

    cribValues = {
        "A": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "10": "10",
        "J": "10",
        "Q": "10",
        "K": "10",
    }

    handSuit = {
        "s": "spade",
        "d": "diamond",
        "h": "heart",
        "c": "club"
    }

    def calculate(self, cards):
        print(1)

    # 2 points per 15 made
    def calc_15(self, cards):
        print(1)

    # 3+ consecutive numbers
    def calc_runs(self, cards):
        print(1)

    # 1 point if in hand 2 points if on turn
    def calc_jack_suit(self, cards):
        print(1)

    # all matching suit in hand or all matching
    # suit in crib hand with matching flip card
    def calc_flush(self, cards):

        for card in cards:
            print(card)

    # 2 points per pair
    def calc_pairs(self, cards):
        print(1)

    def add_points(self):
        print(1)

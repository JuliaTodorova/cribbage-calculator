import itertools
from collections import Counter

class Calculator:
    # transform data to be calculated
    def transform_data(self, players):
        calc_job = []
        # get card objects and transform face cards
        for x in players:
            x.values()
            for i in x.values():
                cards = []
                calc_job.append(cards)
                for p in i:
                    if p.get_value() not in ["Q", "J", "K", "A"]:
                        cards.append(int(p.get_value()))
                    else:
                        cards.append(10)
        return calc_job

    # 2 points per 15 made
    def calc_15(self, calc_job):
        add_to = 15
        result = []
        for x in calc_job:
            result = [
                seq for i in range(len(x), 0, -1)
                for seq in itertools.combinations(x, i)
                if sum(seq) == add_to]
        return result

    # all matching suit in hand or all matching
    def calc_flush(self, players):
        hand = []
        # get card objects and transform face cards
        for x in players:
            x.values()
            for i in x.values():
                cards = []
                hand.append(cards)
                for p in i:
                    cards.append(p.get_suit())

        flush_hands = []
        for x in hand:
            if len(set(x)) == 1:
                flush_hands.append(x)
        return flush_hands

    # 3+ consecutive numbers
    def calc_runs(self, cards):
        print(1)

    # 2 points per pair
    def calc_pairs(self, players):
        all_cards = []
        for x in players:
            for i in x.values():
                cards = []
                all_cards.append(cards)
                for p in i:
                    cards.append(p.get_value())
        count_pairs = []
        for card in all_cards:
            count_pairs.append(Counter(card))
        return count_pairs

    def add_points(self):
        print(1)

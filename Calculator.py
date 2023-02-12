import itertools


class Calculator:
    handSuit = {
        "s": "spade",
        "d": "diamond",
        "h": "heart",
        "c": "club"
    }

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
        for x in calc_job:
            result = [
                seq for i in range(len(x), 0, -1)
                for seq in itertools.combinations(x, i)
                if sum(seq) == add_to]
            return result

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

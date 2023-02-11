import csv
import Players
import Card


class DataHandler:
    # Get CSV game data
    def get_csv_data(self, csvFile):
        data = []

        with open(csvFile, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)

        return data

    # Extract the suit from cards
    def extract_cards(self, cards):
        allCards = []
        card = cards.split(',')
        for x in card:
            value = x.split('-')[0]
            suit = x.split('-')[1]
            one_card = Card.Card(
                    value,
                    suit
            )
            allCards.append(one_card)

        return allCards

    # Create new player objects for each player
    def organize_data(self, file):
        # remove headers
        file.pop(0)

        all_players = []
        for x in file:

            player = x[0]
            cards = x[1]
            crib = x[2]
            score = x[3]

            player = Players.Players(
                player,
                cards,
                crib,
                score
            )

            all_players.append(player)

        return all_players
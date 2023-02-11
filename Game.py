import DataHandler
import Players
import Hand
import Calculator


class Game:

    def play():

        handler = DataHandler.DataHandler()
        file = handler.get_csv_data("cribGame.csv")
        data = handler.organize_data(file)

        cards = []

        for player in data:
            card = player.get_cards()
            cards.append(handler.extract_cards(card))

if __name__ == "__main__":

    Game.play()

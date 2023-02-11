import DataHandler
import Players
import Hand
import Calculator


class Game:

    def play():
        handler = DataHandler.DataHandler()
        file = handler.get_csv_data("cribGame.csv")
        data = handler.organize_data(file)

        players = []

        for player in data:
            cards = player.get_cards()
            cList = handler.extract_cards(cards)
            player_cards = {
                player: cList
            }

            players.append(player_cards)

        print(players)


if __name__ == "__main__":
    Game.play()

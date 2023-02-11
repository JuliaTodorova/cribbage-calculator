import csv
import Players


class DataHandler:
    def getCSVData(self, csvFile):
        data = []

        with open(csvFile, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)

        return data

    def organizeData(self, file):
        # remove headers
        file.pop(0)

        allPlayers = []
        for x in file:
            player = Players.Players(
                x[0],
                x[1],
                x[2],
                x[3]
            )
            allPlayers.append(player)

        for x in allPlayers:
            print(x.print_player())
        return allPlayers


if __name__ == "__main__":
    handler = DataHandler()
    test = handler.getCSVData("cribGame.csv")

    orgData = handler.organizeData(test)

    #print(orgData)

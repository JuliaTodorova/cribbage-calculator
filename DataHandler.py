import csv


class DataHandler:
    def getCSVData(self, csvFile):
        data = []

        with open(csvFile, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)

        return data

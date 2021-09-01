from datetime import date,timedelta

class connection():
    def __init__(self, stations,date,deparr,duration,transfers):
        self.stations=stations
        self.date=date
        self.deparr=deparr
        self.duration=duration
        self.transfers=int(transfers)

class resultsPage:

    def __init__(self, browser):
        self.browser = browser
        self.bestConnections = []
        self.tomorrow = date.today() + timedelta(days=1)
        self.tomorrow = self.tomorrow.strftime("%d.%m.%y")

    def rowsFromResultsTable(self):
        table = self.browser.find_element_by_xpath(("//table[@id='wyniki']/tbody"))
        rows = table.find_elements_by_tag_name("tr")
        return rows

    def createConnectionObject(self, row):
        cels = row.find_elements_by_tag_name("td")
        conn = connection(cels[1].text, cels[2].text, cels[3].text, cels[4].text, cels[5].text)
        return conn

    def printResults(self):
        print("\n\n************** RESULTS **************\n")
        print("Number of connections with the least number of transfers: " + str(len(self.bestConnections)))
        for count, item in enumerate(self.bestConnections):
            print(str(count + 1) + ")")
            print("Stations: " + item.stations)
            print("Date: " + item.date)
            print("Departure/Arrive: " + item.deparr)
            print("Travel time: " + item.duration)
            print('\033[1m' + "Transfers: " + str(item.transfers) + '\033[0m')

    def findBestConnection(self):
        rows = self.rowsFromResultsTable()
        connectionsList = []

        for row in rows:
            conn = self.createConnectionObject(row)
            connectionsList.append(conn)

        bc = 100

        for count, item in enumerate(connectionsList):
            if(item.transfers < bc):
                if (self.tomorrow == item.date):
                    self.bestConnections.clear()
                    self.bestConnections.append(item)
                    bc = item.transfers
            else:
                if(item.transfers == bc):
                    if (self.tomorrow == item.date):
                        self.bestConnections.append(item)

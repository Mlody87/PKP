from selenium.webdriver import ActionChains

class pkpSearchPage:
    URL = 'https://rozklad-pkp.pl'

    def __init__(self, browser):
        self.browser = browser

    def closeAdds(self):
        xPath = "//span[@class='anchor_close']"
        adds = self.browser.find_element_by_xpath(xPath)
        return adds

    def fromStation(self):
        return self.browser.find_element_by_id("from-station")

    def fromStationList(self, fromStation):
        xPath = "//a[@class='ui-corner-all' and contains(text(), '"+fromStation+"')]"
        station = self.browser.find_element_by_xpath(xPath)
        return station

    def toStation(self):
        return self.browser.find_element_by_id("to-station")

    def toStationList(self, toStation):
        xPath = "//a[@class='ui-corner-all' and contains(text(), '"+toStation+"')]"
        station = self.browser.find_element_by_xpath(xPath)
        return station

    def nextDay(self):
        xPath = "//img[contains(@alt, 'Dzień później')]//.."
        return self.browser.find_element_by_xpath(xPath)

    def hour(self):
        return self.browser.find_element_by_id("hour")

    def submit(self):
        button = self.browser.find_element_by_id("singlebutton")
        return button

    def load(self):
        self.browser.get(self.URL)

    def eatCookies(self):
        xPath = "//button[@aria-label='ZGADZAM SIĘ']"
        cookie = self.browser.find_element_by_xpath(xPath)
        return cookie

    def searchConnection(self, fromTown, toTown):
        self.fromStation().send_keys(fromTown)
        self.fromStationList(fromTown).click()
        self.toStation().send_keys(toTown)
        self.toStationList(toTown).click()
        self.hour().send_keys("00:00")
        self.nextDay().click()
        actions = ActionChains(self.browser)
        actions.move_to_element(self.submit()).perform()
        self.submit().click()

import pytest
from selenium.webdriver import Chrome
from pages import searchPage
from pages import resultsPage

@pytest.fixture
def browser():
    driver = Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")
    driver.implicitly_wait(15)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_minNumberOfTransfers(browser):
    search = searchPage.pkpSearchPage(browser)
    search.load()
    search.eatCookies().click()
    search.closeAdds().click()
    search.searchConnection("Kraków Główny", "Lausanne")

    results = resultsPage.resultsPage(browser)
    results.findBestConnection()
    results.printResults()

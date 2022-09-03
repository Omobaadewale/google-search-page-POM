from pages.main_page import MainPage
from pages.base_page import Page
from pages.search_page import Search

class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.base_page = Page(self.driver)
        self.search_page = Search(self.driver)


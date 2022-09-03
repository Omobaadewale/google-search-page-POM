from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from selenium.webdriver.support.ui import Select


class MainPage(Page):
    SEARCH_INPUT = (By.CSS_SELECTOR, "div.YacQv.gsfi")
    SEARCH_BTN =   (By.CSS_SELECTOR, 'span.QCzoEc')
    search_word = "amapiano"

    def open_main_page(self):
        self.open_page()


    def search_page(self):
        pass


    #def search_google(self, search_word):
     #   self.input_text(search_word,*self.SEARCH_INPUT)
      #  self.click(*self.SEARCH_BTN)








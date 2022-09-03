from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.keys import Keys


class Search(Page):
    SEARCH_INPUT = (By.CSS_SELECTOR, "input.gLFyf.gsfi")
    SEARCH_BTN = (By.CSS_SELECTOR, "input.gLFyf.gsfi")
    search_word = "amapiano"
    expected_result = 'Amapiano'
    AMAPIANO_RESULT = (By.XPATH, "//span[text()='Amapiano']")
    SEARCH_INPUT_LAPTOPS = (By.XPATH,"//span[text()='Shop laptops']")
    search_word_laptops = "laptops"
    expected_result_laptops = 'Shop laptops'



    def search_google(self, search_word):
        self.input_text(search_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)
        self.input_text(Keys.ENTER,*self.SEARCH_INPUT)


    def search_laptops(self, search_word_laptops):
        self.input_text(search_word_laptops, *self.SEARCH_INPUT_LAPTOPS)
        self.click(*self.SEARCH_INPUT)


    def verify_result(self):
        expected_result = 'Amapiano'
        actual_result = self.driver.find_element(*self.AMAPIANO_RESULT).text
        assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected{expected_result}'


    #def verify_result_laptops(self):
     #   expected_result_laptops = 'Shop laptops'
      #  actual_result = self.driver.find_element(*self.SEARCH_INPUT_LAPTOPS).text
       # assert self.expected_result_laptops == actual_result, f'Error! Actual text {actual_result} does not match expected{self.expected_result_laptops}'



    def click_enter(self):
        self.input_text(*self.SEARCH_BTN)





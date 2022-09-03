from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

@given('Open google page')
def open_google(context):
    context.app.main_page.open_main_page()


@when('Search for {search_word}')
def search_google(context, search_word):
    context.app.search_page.search_google(search_word)



#@then('Verify search result for {expected_result_laptops} is shown')
#def verify_result_laptop(context, expected_result_laptops):
 #   context.app.search_page.verify_result_laptops()
  #  sel


@then("user clicks enter")
def click_enter(context):
    context.app.search_page.click_enter()


@then("Verify search result for {expected_result} is shown")
def verify_result(context, expected_result):
    context.app.search_page.verify_result()

    print("Test case passed")

from behave import *
from selenium.webdriver import Keys

from components.search import Search


@step('Navigate to {url}')
def step_impl(context, url):
    context.driver.get(url)


@step("UI: Input {user_name} into search field")
def step_impl(context, user_name):
    context.search = Search(context.driver)
    context.search.search_field_input(user_name)


@step("UI: Push Enter key")
def step_impl(context):
    context.search.search_field_input(Keys.RETURN)


@step("UI: Click Search button")
def step_impl(context):
    context.search.click_search_button()


@step("UI: refresh page")
def step_impl(context):
    context.search.page_refresh()

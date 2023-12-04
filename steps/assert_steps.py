from behave import *
from jsonpath_ng import jsonpath, parse
import json
import requests
from components.xpath_locators import Locators
from components.json_locators import JsonLocators


@then("Verify repos field values")
def step_impl(context):
    api_repo_number = context.response.json()["public_repos"]
    ui_repo_number = context.search.get_text(Locators.number_of_repos)
    assert str(api_repo_number) == ui_repo_number


@step("API: verify status code is {status_code}")
def step_impl(context, status_code):
    assert (context.response.status_code == int(status_code))


@then("Varify empty results: no article element on the page")
def step_impl(context):
    elements = "article"
    source = context.search.get_page_source()
    assert elements not in source


    # file_name = JsonLocators.file_name
    # with open(file_name, 'r') as json_file:
    #     file_data = json.load(json_file)
    #
    # # JSONPath expression to get all book titles
    # expression = parse("$.store.book[*].title")
    #
    # # Apply the expression to the JSON data
    # matches = [match.value for match in jsonpath(json_data, expression)]
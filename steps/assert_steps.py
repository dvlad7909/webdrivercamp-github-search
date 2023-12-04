from behave import *
from jsonpath_ng import jsonpath, parse
import json
import requests
from components.xpath_locators import Locators
from components.json_locators import JsonLocators


@then("Verify {field} field values")
def step_impl(context, field):
    ui_repo_number = None
    expression = None
    match field:
        case 'repos':
            ui_repo_number = context.search.get_text(Locators.number_of_repos)
            expression = parse("$.public_repos")

    file_name = JsonLocators.file_name
    with open(file_name, 'r') as json_file:
        json_data = json.load(json_file)
    # JSONPath expression

    # Apply the expression to the JSON data
    api_repo_number = [match.value for match in expression.find(json_data)][0]

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

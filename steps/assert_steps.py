import time

from behave import *
from jsonpath_ng import jsonpath, parse
import json
import requests

from components.search import Search
from components.xpath_locators import Locators
from components.json_locators import JsonLocators


@then("Verify {field} field values")
def step_impl(context, field):
    ui_numbers = None
    expression = None
    match field:
        case 'repos':
            ui_numbers = Search(context.driver).get_text(Locators.number_of_repos)
            expression = parse(JsonLocators.number_of_repos_json)
        case 'followers':
            ui_numbers = Search(context.driver).get_text(Locators.number_of_followers)
            expression = parse(JsonLocators.number_of_followers_json)
        case 'following':
            ui_numbers = Search(context.driver).get_text(Locators.number_of_following)
            expression = parse(JsonLocators.number_of_following_json)
        case 'gists':
            ui_numbers = Search(context.driver).get_text(Locators.number_of_gists)
            expression = parse(JsonLocators.number_of_gists_json)

    file_name = JsonLocators.file_name
    with open(file_name, 'r') as json_file:
        json_data = json.load(json_file)
    # JSONPath expression

    # Apply the expression to the JSON data
    api_numbers = [match.value for match in expression.find(json_data)][0]

    assert str(api_numbers) == ui_numbers


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


@then("Verify {parameter} of followers")
def step_impl(context, parameter):
    followers_xpath = Locators.followers_list
    time.sleep(0.5)
    items = context.search.get_elements(followers_xpath)
    item_features = []
    item_list = []
    item_list.extend(i for i in items)
    for i in range(1, len(item_list) + 1):
        name_xpath = f"{followers_xpath}[{str(i)}]//child::h4"
        link_xpath = f"{followers_xpath}[{str(i)}]//child::a"
        item_name = context.search.get_text(name_xpath)
        item_link = context.search.get_text(link_xpath)
        item_features.append({"name": item_name, "link": item_link})

    with open('json_response.json', 'r') as json_file:
        json_data = json.load(json_file)
    expression = parse(JsonLocators.followers_logins_json)
    logins = [match.value.lower() for match in expression.find(json_data)]
    expression = parse(JsonLocators.followers_links_json)
    links = [match.value.lower() for match in expression.find(json_data)]

    match parameter:
        case 'number':
            number_of_followers_ui = len(item_features)
            number_of_followers_api = len(logins)
            assert number_of_followers_ui == number_of_followers_api

        case 'logins':
            logins_ui = []
            for i in item_features:
                logins_ui.append(i['name'].lower())
            logins_api = logins
            assert logins_api == logins_ui

        case 'links':
            links_ui = []
            for i in item_features:
                links_ui.append(i['link'].lower())
            links_api = links
            print(links_api)
            print(links_ui)
            assert links_api == links_ui

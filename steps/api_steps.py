from behave import *
import json
import requests

import components.git_token
from components.json_locators import JsonLocators


@step("API: send get request to {user_name}")
def step_impl(context, user_name):
    repo_url = f"https://api.github.com/users/{user_name}"
    context.response = requests.get(repo_url)

    file_name = JsonLocators.file_name
    json_data = context.response.json()

    with open(file_name, "w") as write_file:
        json.dump(json_data, write_file)


@step("API: send post request to {user_name} to add 1 more repo")
def step_impl(context, user_name):
    repo_url = 'https://api.github.com/user/repos'
    token = f'token {components.git_token.GitToken.git_token}'
    header_content = {'Authorization': token}
    payload = {
        'name': 'repo-created-with-api',
        'private': False,
        'has_wiki': False
    }

    context.response = requests.post(repo_url, headers=header_content, json=payload)

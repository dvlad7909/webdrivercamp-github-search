from behave import *
import json
import requests
from components.json_locators import JsonLocators


@step("API: send get request to {user_name} repo")
def step_impl(context, user_name):
    repo_url = f"https://api.github.com/users/{user_name}"
    context.response = requests.get(repo_url)

    file_name = JsonLocators.file_name
    json_data = context.response.json()

    with open(file_name, "w") as write_file:
        json.dump(json_data, write_file)

    print(repo_url)
    print(context.response.status_code)




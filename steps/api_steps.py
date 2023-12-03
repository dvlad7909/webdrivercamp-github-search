from behave import *
import json
import requests


@step("API: send get request to {user_name} repo")
def step_impl(context, user_name):
    repo_url = f"https://api.github.com/users/{user_name}"
    print(repo_url)
    context.response = requests.get(repo_url)
    print(context.response.status_code)




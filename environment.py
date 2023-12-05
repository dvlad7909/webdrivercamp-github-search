from selenium import webdriver
import requests
import components.git_token


def before_feature(context, feature):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


def after_feature(context, feature):
    context.driver.close()


def after_scenario(context, scenario):
    match scenario.name:

        case "Verify repos data is updated on page refresh":
            token = f'token {components.git_token.GitToken.git_token}'
            header_content = {'Authorization': token}
            owner = 'dvlad7909'
            repo = 'repo-created-with-api'
            url = f'https://api.github.com/repos/{owner}/{repo}'
            response = requests.delete(url, headers=header_content)

        case "Verify gists data is updated on page refresh":
            g_id = context.feature.gist_id
            token = f'token {components.git_token.GitToken.gists_token}'
            url = f'https://api.github.com/gists/{g_id}'
            header_content = {'Authorization': token}
            response = requests.delete(url, headers=header_content)

        case _:
            pass

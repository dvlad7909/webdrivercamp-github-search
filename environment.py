from selenium import webdriver
from base.environment import hooks
from behave import fixture

from components.git_components import GitComponents

from base.steps.api_steps import *


def before_all(context):
    hooks.before_all(context)


def after_all(context):
    hooks.after_all(context)


def before_feature(context, feature):
    if 'no_browser' not in feature.tags:
        context.driver = webdriver.Chrome()
        context.driver.maximize_window()
        context.driver.implicitly_wait(2)

    hooks.before_feature(context, feature)


def after_feature(context, feature):
    if 'no_browser' not in feature.tags:
        context.driver.close()
    hooks.after_feature(context, feature)


def before_scenario(context, scenario):
    hooks.before_scenario(context, scenario)


def after_scenario(context, scenario):
    hooks.after_scenario(context, scenario)


def before_step(context, step):
    hooks.before_step(context, step)


def after_step(context, step):
    hooks.after_step(context, step)


def after_tag(context, tag):
    git = GitComponents()
    match tag:

        case "del_repo":
            git.delete_repo()

        case "del_gist":
            git.delete_gist(context)

        case "del_following":
            git.delete_following()

        case _:
            pass

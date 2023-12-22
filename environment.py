from selenium import webdriver
from behave import fixture

from components.git_components import GitComponents

from base.steps.api_steps import *

#
# def before_feature(context, feature):
#     context.driver = webdriver.Chrome()
#     context.driver.maximize_window()
#     context.driver.implicitly_wait(2)
#
#
# def after_feature(context, feature):
#     context.driver.close()
#
#
# def after_tag(context, tag):
#     git = GitComponents()
#     match tag:
#
#         case "del_repo":
#             git.delete_repo()
#
#         case "del_gist":
#             git.delete_gist(context)
#
#         case "del_following":
#             git.delete_following()
#
#         case _:
#             pass

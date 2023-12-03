from behave import *
from jsonpath_ng import jsonpath, parse
import json
import requests


@then("Verify repos field values")
def step_impl(context):
    api_repo_number = context.response.json()["public_repos"]
    ui_repo_number = context.search.get_text("//p[contains(text(), 'repos')]//preceding-sibling::h3")
    assert str(api_repo_number) == ui_repo_number


@step("API: verify status code is {status_code}")
def step_impl(context, status_code):
    assert (context.response.status_code == int(status_code))


@then("Varify empty results: no article element on the page")
def step_impl(context):

    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Varify empty results: no article element on the page')
from behave import *


@then("Verify repos field values")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Verify repos field values')


@step("API: verify status code is {status_code}")
def step_impl(context, status_code):
    assert context.response.status_code == status_code

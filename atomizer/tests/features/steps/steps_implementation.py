from behave import *


@given('we have behave "{name}"')
def step_impl(context, name):
    print(name)


@when('we implement test number "{numeral:d}"')
def step_impl(context, numeral):
    assert type(numeral) is int


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False

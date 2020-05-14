from behave import *


@given('we have behave "{name}"')  # noqa
def step_impl(context, name):  # noqa
    print(name)


@when('we implement test number "{numeral:d}"')  # noqa
def step_impl(context, numeral):  # noqa
    assert type(numeral) is int


@then('behave will test it for us!')  # noqa
def step_impl(context):  # noqa
    assert context.failed is False

from behave import given, then, when, use_step_matcher


use_step_matcher("re")

@given('we have behave "(?P<name>\w+)"')  # noqa
def step_impl(context, name):  # noqa
    print(name)


@when('we implement test number "(?P<numeral>\d+)"')  # noqa
def step_impl(context, numeral):  # noqa
    try:
        numeral = int(numeral)
        print(numeral)
    except ValueError:
        context.failed = True


@when('we implement test number "(?P<word>\w+)"')  # noqa
def step_impl(context, word):  # noqa
    print(word)
    assert type(word) is str


use_step_matcher("parse")


@when('we run test number "{value:d}"')  # noqa
def step_impl(context, value):  # noqa
    print(value)
    assert type(value) is int


@then('behave will test it for us!')  # noqa
def step_impl(context):  # noqa
    assert context.failed is False

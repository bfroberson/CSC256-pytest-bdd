import pytest
from pytest_bdd import scenario, parsers, given, when, then
from retirement1 import Retirement


@scenario('../features/retirement.feature', 'Search for retirement age')
def test_retirement_app():
    pass


@given('a retirement age app')
def retirement():
    return Retirement('1900', '1')


@when(parsers.parse('the user enters {year:d} and {month:d}'), converters=dict(year=str, month=str))
def input_retirement_year_and_month(retire, year, month):
    retire.set_year(year)
    retire.set_month(month)


@then(parsers.parse('the {retirement_year:d}, {retirement_month:d}, '
                    '{end_month:d} and {end_year:d} are shown'))
def full_retirement(retire, retirement_year, retirement_month, end_month, end_year):
    assert retire.fullRetirement() == f'Your full retirement age {retirement_year} ' \
                                      f'is and {retirement_month} months\n' \
                                      f'This will be in {end_month} of {end_year}'


@scenario('../features/retirement.feature', 'Search for retirement age')
def test_retirement_app():
    pass


@given('a retirement age app')
def retirement():
    return Retirement('1900', '1')


@when(parsers.parse('the user enters {invalid_year:d} and/or {invalid_month:d}'), converters=dict(year=str, month=str))
def input_retirement_year_and_month(retire, invalid_year, invalid_month):
    retire.set_year(invalid_year)
    retire.set_month(invalid_month)


@then('an error message is shown')
def full_retirement(retire):
    assert retire.fullRetirement() == 'Age must be between 1900 and current year'

Feature: Retirement Calculator
    As a user, I want to find out how old I have to be for full retirement.

    Scenario Outline: Search for retirement age
        Given a retirement age app
        When the user enters "<year>" and "<month>"
        Then the "<retirement_year>", "<retirement_month>", "<end_month>", and "<end_year>" are shown

        Examples: Vertical
            |      year        | 1957 | 1937  |
            |      month       | 12   | 4     |
            |  retirement_year | 66   | 65    |
            | retirement_month | 6    | 0     |
            |    end_month     | June | April |
            |    end_year      | 2024 | 2002  |

    Scenario Outline: Search for retirement age using invalid inputs
        Given a retirement age app
        When the user enters "<invalid_year> and/or "<invalid_month"
        Then an error message is shown

        Examples: Vertical
            | invalid_year  | 1899 | 2022 | 1990 | 2003 |
            | invalid_month | 12   | 8    | 13   | 0    |


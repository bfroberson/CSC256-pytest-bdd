from datetime import datetime


def main():
    print("Social Security Full Retirement Age Calculator")
    print()

    year = input("Enter year of birth: ")

    month = input("Enter the month of birth: ")
    print()

    retire = Retirement(year, month)
    retire.fullRetirement()


class Retirement:
    def __init__(self, year, month):
        self.__year = year
        self.__month = month
        self.__age = 0
        self.__monthString = ''
        self.__retirementYear = 0

    # Helper method
    def __getRetirementAge(self):

        retirementAge = {
            "1900" <= self.__year < "1938": "65 and 0 months",
            self.__year == "1938": "65 and 2 months",
            self.__year == "1939": "65 and 4 months",
            self.__year == "1940": "65 and 6 months",
            self.__year == "1941": "65 and 8 months",
            self.__year == "1942": "65 and 10 months",
            "1942" < self.__year < "1955": "66 and 0 months",
            self.__year == "1955": "66 and 2 months",
            self.__year == "1956": "66 and 4 months",
            self.__year == "1957": "66 and 6 months",
            self.__year == "1958": "66 and 8 months",
            self.__year == "1959": "66 and 10 months",
            "1960" < self.__year <= str(datetime.now().strftime("%Y")): "67 and 0 months"
        }

        return retirementAge

    def fullRetirement(self):
        try:
            self.__age = self.__getRetirementAge().get(True)

            if self.__age is None:
                print("Age must be between 1900 and current year")
            elif int(self.__month) < 1 or int(self.__month) > 12:
                print("Month must be between 1 and 12")
            else:
                try:
                    retirementAgeList = self.__age.split(" ")

                    retirementMonth = int("".join(retirementAgeList[2])) + int(self.__month)

                    self.__retirementYear = int(self.__year) + int(retirementAgeList[0])

                    if retirementMonth > 12:
                        retirementMonth = retirementMonth % 12
                        self.__retirementYear += 1

                    self.__monthString = datetime(int(self.__year), int(retirementMonth), 1).strftime("%B")
                    self.__str__()
                except (OverflowError, ValueError):
                    print("Invalid input")
        except(ValueError, OverflowError, TypeError):
            print("Input error")

    def set_year(self, year):
        self.__year = year

    def set_month(self, month):
        self.__month = month

    def __str__(self):
        print("Your full retirement age is " + str(self.__age) +
              "\nThis will be in " + self.__monthString + " of " + str(self.__retirementYear))


if __name__ == '__main__':
    main()

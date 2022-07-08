# Во вложении файл csv с данными про аэропорты мира, написать программу которая
# сможет вернуть данные по таким параметрам:
#
# --iata_code - код аэропорта, должно вернуть 1 запись по коду
# аэропорта(всю строку) или вернуть ошибку AirportNotFoundError
# --country - страна, должно вернуть все записи по аэропортам или
# CountryNotFoundError
# --name - значение имени аэропорта, допустимо вхождение строки хотябы
# минимально, т.е. liman должен вернуть строки с такими названиями:
# Ilimanaq Heliport
# Sidi Slimane Airport
# Kilimanjaro International Airport
# West Kilimanjaro Airport
# Limanske Airfield
# Liman Airfield
# ...
# или AirportNotFoundError
#
# Только один параметр обязателен, если выбрано несколько - вернуть
# ошибку:
# MultipleOptionsError, если ни одного - NoOptionsFoundError
# ** доп. ошибки принимают два аргумента, текст ошибки и входные данные,
#
# пример:
#
# AirportNotFoundError: ('Airport not found', 'OESD')
# CountryNotFoundError: ('Country not found', 'UGUGU')
# IATA код может быть только 3х буквенным в верхнем регистре, сделать валидацию
# на него или вернуть IATACodeError
import argparse
import csv
import re
import click


class NoOptionsFoundError(Exception):
    def __init__(self):
        self.txt = "One argument required."

    def __str__(self):
        return self.txt


class MultipleOptionsError(Exception):
    def __init__(self, num):
        self.txt = f'{num} arguments entered. Only one argument required.'

    def __str__(self):
        return self.txt


class IATACodeError(Exception):
    def __init__(self, iata_code):
        self.txt = f'"{iata_code}" is incorrect format. Should be three ' \
                   f'capital letters.'

    def __str__(self):
        return self.txt


class AirportNotFoundError(Exception):
    def __init__(self, parameter):
        self.txt = f'"{parameter}", Airport not found'

    def __str__(self):
        return self.txt


class CountryNotFoundError(Exception):
    def __init__(self, country):
        self.txt = f'"{country}", Country not found'

    def __str__(self):
        return self.txt


@click.command()
@click.option('-ic', '--iata_code')
@click.option('-c', '--country')
@click.option('-n', '--name')
def main(iata_code, country, name):
    def check_args_quantity():
        my_args = len([ar for ar in [iata_code, country, name] if ar
                       is not None])
        if my_args == 0:
            raise NoOptionsFoundError
        if my_args > 1:
            raise MultipleOptionsError(my_args)

    def iata_code_validation():
        if iata_code:
            if not re.fullmatch(r'[A-Z]{3}', iata_code):
                raise IATACodeError(iata_code)

    check_args_quantity()
    iata_code_validation()
    program = AirportSearch(iata_code, country, name)
    print(program)


class AirportSearch:
    def __init__(self, iata_code, country, name):
        self.iata_code = iata_code
        self.country = country
        self.name = name

    def __repr__(self):
        if self.iata_code:
            return f'{self.find_iata_code()}'
        if self.country:
            return "\n".join(str(self.find_country()).split("}"))
        if self.name:
            return "\n".join(str(self.find_name()).split("}"))

    def extract_info(self):
        airports_info = []
        with open('airport-codes_csv.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                airports_info.append(row)
        return airports_info

    def find_iata_code(self):
        for row in self.extract_info():
            if row['iata_code'] == self.iata_code.upper():
                return row
        raise AirportNotFoundError(self.iata_code)

    def find_country(self):
        airports_in_country = []
        for row in self.extract_info():
            if row['iso_country'] == self.country:
                airports_in_country.append(row)
        if not airports_in_country:
            raise CountryNotFoundError(self.country)
        return airports_in_country

    def find_name(self):
        list_of_names = []
        for row in self.extract_info():
            if re.match(self.name.lower(), row['name'].lower()):
                list_of_names.append(row)
        if not list_of_names:
            raise AirportNotFoundError(self.name)
        return list_of_names


if __name__ == '__main__':
    main()


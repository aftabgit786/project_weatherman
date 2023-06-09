import argparse
from datetime import datetime
import calendar

from utils import read_file_for_e, read_files
from constants import MappingIndex


def calculate_temperature_and_humidity(year):
    file_values = read_file_for_e(year)

    maximum_temperature = None
    minimum_temperature = None
    humidity = None

    for file_value in file_values:
        full_date = file_value[MappingIndex.DATE]
        max_temp = file_value[MappingIndex.MAXIMUM_TEMPERATURE]
        min_temp = file_value[MappingIndex.MINIMUM_TEMPERATURE]
        humid = file_value[MappingIndex.HUMIDITY]

        split_date = full_date.split("-")
        sliced_date = int(split_date[MappingIndex.SLICED_DATE])

        datetime_object = datetime.strptime(full_date, "%Y-%m-%d")
        month_name = datetime_object.strftime("%B")

        if min_temp and (minimum_temperature is None or int(min_temp) < minimum_temperature):
            minimum_temperature = int(min_temp)
            date_for_minimum_temperature = sliced_date
            month_name_for_minimum_temperature = month_name

        if max_temp and (maximum_temperature is None or int(max_temp) > maximum_temperature):
            maximum_temperature = int(max_temp)
            date_for_maximum_temperature = sliced_date
            month_name_for_maximum_temperature = month_name

        if humid and (humidity is None or int(humid) > humidity):
            humidity = int(humid)
            date_for_humidity = sliced_date
            month_name_for_humidity = month_name

    print(f"Highest: {maximum_temperature}°C on {month_name_for_maximum_temperature} {date_for_maximum_temperature}")
    print(f"Lowest: {minimum_temperature}°C on {month_name_for_minimum_temperature} {date_for_minimum_temperature}")
    print(f"Humidity: {humidity}% on {month_name_for_humidity} {date_for_humidity}")


def calculate_average_temperature_and_humidity(year):
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--date', type=str, help="Date argument in the format 'year/month'")
    args = parser.parse_args()

    year, month_number = args.date.split('/')

    casting = int(month_number)
    month = calendar.month_abbr[casting]

    file_values = read_files(month, year)

    maximum_temperature = None
    minimum_temperature = None
    sum_humidity = 0
    humidity_count = 0
    average_humidity = 0

    for file_value in file_values:
        average_temp = file_value[MappingIndex.AVERAGE_TEMPERATURE]
        humidity = file_value[MappingIndex.AVERAGE_HUMIDITY]

        if average_temp:
            if minimum_temperature is None or int(average_temp) < minimum_temperature:
                minimum_temperature = int(average_temp)
            if maximum_temperature is None or int(average_temp) > maximum_temperature:
                maximum_temperature = int(average_temp)

            if humidity:
                sum_humidity += int(humidity)
                humidity_count += 1

        if humidity_count:
            average_humidity = sum_humidity / humidity_count

    print(f"Highest Average: {maximum_temperature}°C")
    print(f"Lowest Average: {minimum_temperature}°C")
    print(f"Average Mean Humidity: {average_humidity}%")


def draw_chart_of_temperature_in_tow_lines(year):
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--date', type=str, help="Date argument in the format 'year/month'")
    args = parser.parse_args()

    year, month_number = args.date.split('/')

    casting = int(month_number)
    month = calendar.month_abbr[casting]

    file_values = read_files(month, year)

    red_code = '\033[91m'
    blue_code = '\033[34m'
    reset_code = '\033[0m'

    for file_value in file_values:
        date = file_value[MappingIndex.DATE]
        sliced_date = date.split('-')[MappingIndex.SLICED_DATE]
        maximum_temperature = file_value[MappingIndex.MAXIMUM_TEMPERATURE]
        minimum_temperature = file_value[MappingIndex.MINIMUM_TEMPERATURE]

        if maximum_temperature and minimum_temperature is not None:
            print(f"{sliced_date}{red_code}{int(maximum_temperature) * '+'}{reset_code} {maximum_temperature}C")
            print(f"{sliced_date}{blue_code}{int(minimum_temperature) * '+'}{reset_code} {minimum_temperature}C")


def draw_chart_multiple_time(year):
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--date', type=str, help="Date argument in the format 'year/month'")
    args = parser.parse_args()

    year, month_number = args.date.split('/')

    casting = int(month_number)
    month = calendar.month_abbr[casting]

    file_values = read_files(month, year)

    for number in range(5):

        for file_value in file_values:
            date = file_value[MappingIndex.DATE]
            sliced_date = date.split('-')[MappingIndex.SLICED_DATE]
            maximum_temperature = file_value[MappingIndex.MAXIMUM_TEMPERATURE]
            minimum_temperature = file_value[MappingIndex.MINIMUM_TEMPERATURE]

            if maximum_temperature and minimum_temperature is not None:
                print(f"{sliced_date}{red_code}{int(maximum_temperature) * '+'}{reset_code} {maximum_temperature}C")
                print(f"{sliced_date}{blue_code}{int(minimum_temperature) * '+'}{reset_code} {minimum_temperature}C")


def draw_chart_of_temperature_in_one_line(year):
    parser.add_argument('-c', '--date', type=str, help="Date argument in the format 'year/month'")
    args = parser.parse_args()

    year, month_number = args.date.split('/')

    casting = int(month_number)
    month = calendar.month_abbr[casting]

    file_values = read_files(month, year)

    for file_value in file_values:
        date = file_value[MappingIndex.DATE]
        sliced_date = date.split('-')[MappingIndex.SLICED_DATE]
        maximum_temperature = file_value[MappingIndex.MAXIMUM_TEMPERATURE]
        minimum_temperature = file_value[MappingIndex.MINIMUM_TEMPERATURE]

        if maximum_temperature and minimum_temperature is not None:
            print(f"{sliced_date}{blue_code}{int(minimum_temperature) * '+'}{red_code}{int(maximum_temperature) * '+'}"
                  f"{reset_code} {minimum_temperature}C - {maximum_temperature}C")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--year', type=str, help='Specify the year')
    args = parser.parse_args()

    year = args.year
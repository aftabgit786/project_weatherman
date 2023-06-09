import argparse
import calendar

from utils import read_files
from constants import MappingIndex


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

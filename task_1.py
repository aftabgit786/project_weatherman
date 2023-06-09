import argparse
from datetime import datetime

from utils import read_file_for_e
from constants import MappingIndex

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--year', type=str, help='Specify the year')
args = parser.parse_args()

year = args.year

file_values = read_file_for_e(year)

maximum_temperature = None
minimum_temperature = None
humidity = None
month_name_for_maximum_temperature = None
date_for_maximum_temperature = None
month_name_for_minimum_temperature = None
date_for_minimum_temperature = None
month_name_for_humidity = None
date_for_humidity = None

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

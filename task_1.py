from datetime import datetime
from utils import read_files
from constant import MappingIndex


year = input("Enter year: ")
file_values = read_files(year)

maximum_temperature = None
minimum_temperature = None
humidity = None
date_for_maximum_temperature = None
date_for_minimum_temperature = None
date_for_humid = None
month_name_for_maximum_temperature = None
month_name_for_minimum_temperature = None
month_name_for_humid = None

for file_value in file_values:
    full_date = file_value[MappingIndex.date]
    max_temp = file_value[MappingIndex.maximum_temperature]
    min_temp = file_value[MappingIndex.minimum_temperature]
    humid = file_value[MappingIndex.humidity]
    split_date = full_date.split("-")
    sliced_date = int(split_date[MappingIndex.sliced_date])
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
        date_for_humid = sliced_date
        month_name_for_humid = month_name

print(f"Highest: {maximum_temperature}°C on {month_name_for_maximum_temperature} {date_for_maximum_temperature}")
print(f"Lowest: {minimum_temperature}°C on {month_name_for_minimum_temperature} {date_for_minimum_temperature}")
print(f"Humidity: {humidity}% on {month_name_for_humid} {date_for_humid}")

from datetime import datetime
from utils import read_files


file_values = read_files()

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
    full_date = file_value[0]
    max_temp = file_value[1]
    min_temp = file_value[3]
    humid = file_value[7]
    split_date = full_date.split("-")
    month_num = int(split_date[1])
    date = int(split_date[2])
    datetime_object = datetime.strptime(full_date, "%Y-%m-%d")
    month_name = datetime_object.strftime("%B")

    if min_temp.isdigit() and (minimum_temperature is None or int(min_temp) < minimum_temperature):
        minimum_temperature = int(min_temp)
        date_for_minimum_temperature = date
        month_name_for_minimum_temperature = month_name

    if max_temp.isdigit() and (maximum_temperature is None or int(max_temp) > maximum_temperature):
        maximum_temperature = int(max_temp)
        date_for_maximum_temperature = date
        month_name_for_maximum_temperature = month_name

    if humid.isdigit() and (humidity is None or int(humid) > int(humidity)):
        humidity = humid
        date_for_humid = date
        month_name_for_humid = month_name

print(f"Highest: {maximum_temperature}°C on {month_name_for_maximum_temperature} {date_for_maximum_temperature}")
print(f"Lowest: {minimum_temperature}°C on {month_name_for_minimum_temperature} {date_for_minimum_temperature}")
print(f"Humidity: {humidity}% on {month_name_for_humid} {date_for_humid}")

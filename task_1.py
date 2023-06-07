from datetime import datetime
from utils import read_files


file_values = read_files()

max_temperature = None
min_temperature = None
humidity = None
date_for_max = None
date_for_min = None
date_for_humid = None
month_name_for_max = None
month_name_for_min = None
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

    if min_temp.isdigit() and (min_temperature is None or int(min_temp) < min_temperature):
        min_temperature = int(min_temp)
        date_for_min = date
        month_name_for_min = month_name

    if max_temp.isdigit() and (max_temperature is None or int(max_temp) > max_temperature):
        max_temperature = int(max_temp)
        date_for_max = date
        month_name_for_max = month_name

    if humid.isdigit() and (humidity is None or int(humid) > int(humidity)):
        humidity = humid
        date_for_humid = date
        month_name_for_humid = month_name

print(f"Highest: {max_temperature}°C on {month_name_for_max} {date_for_max}")
print(f"Lowest: {min_temperature}°C on {month_name_for_min} {date_for_min}")
print(f"Humidity: {humidity}% on {month_name_for_humid} {date_for_humid}")

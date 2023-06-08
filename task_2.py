from utils import read_files
from utils import calculate_average_humidity
from constant import MappingIndex


month = input('Enter month: ')
file_values = read_files(month)

maximum_temperature = None
minimum_temperature = None


for file_value in file_values:
    average_temp = file_value[MappingIndex.average_temperature]
    humidity = file_value[MappingIndex.average_humidity]

    if average_temp:
        if minimum_temperature is None or int(average_temp) < minimum_temperature:
            minimum_temperature = int(average_temp)
        if maximum_temperature is None or int(average_temp) > maximum_temperature:
            maximum_temperature = int(average_temp)


average_humidity = calculate_average_humidity(file_values)

print(f"Highest Average: {maximum_temperature}°C")
print(f"Lowest Average: {minimum_temperature}°C")
print(f"Average Mean Humidity: {average_humidity}%")

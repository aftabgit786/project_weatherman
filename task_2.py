from utils import read_files


file_values = read_files()

maximum_temperature = None
minimum_temperature = None
average_humidity = 0
humidity_count = 0

for file_value in file_values:
    full_date = file_value[0]
    average_temp = file_value[2]
    humidity = file_value[8]

    if average_temp.isdigit():
        if minimum_temperature is None or int(average_temp) < minimum_temperature:
            minimum_temperature = int(average_temp)
        if maximum_temperature is None or int(average_temp) > maximum_temperature:
            maximum_temperature = int(average_temp)

    if humidity.isdigit():
        average_humidity += int(humidity)
        humidity_count += 1

if humidity_count > 0:
    average_humidity /= humidity_count

print(f"Highest Average: {maximum_temperature}°C")
print(f"Lowest Average: {minimum_temperature}°C")
print(f"Average Mean Humidity: {average_humidity}%")

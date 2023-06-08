import os
from constant import MappingIndex


def get_file_contents(file_content):
    file_values = []
    for row in file_content.split("\n")[1:-1]:
        file_values.append(row.split(","))
    return file_values


def read_files(data):
    file_values = []
    for file_name in os.listdir("weatherfiles"):
        file_parts = file_name.split("_")
        file_month = file_parts[3].split(".")[0]
        file_year = file_parts[2]
        if file_month == data or file_year == data:
            with open(os.path.join("weatherfiles", file_name), "r") as file_reader:
                file_values += get_file_contents(file_reader.read())
    return file_values


def calculate_average_humidity(file_values):
    average_humidity = 0
    humidity_count = 0

    for file_value in file_values:
        humidity = file_value[MappingIndex.average_humidity]

        if humidity:
            average_humidity += int(humidity)
            humidity_count += 1

    if humidity_count > 0:
        average_humidity /= humidity_count

    return average_humidity

import os

from constants import MappingIndex


def get_file_contents(file_content):
    file_values = []
    for row in file_content.split("\n")[MappingIndex.INDEX_ONE:MappingIndex.INDEX_MINUS_ONE]:
        file_values.append(row.split(","))

    return file_values


def read_file_for_e(year):
    file_values = []
    for file_name in os.listdir(MappingIndex.WEATHER_DIR):
        file_parts = file_name.split("_")
        file_year = file_parts[MappingIndex.INDEX_TOW]
        if file_year == year:
            with open(os.path.join(MappingIndex.WEATHER_DIR, file_name), "r") as file_reader:
                file_values += get_file_contents(file_reader.read())

    return file_values


def read_files(month, year):
    file_values = []
    for file_name in os.listdir(MappingIndex.WEATHER_DIR):
        file_parts = file_name.split("_")
        file_year = file_parts[MappingIndex.INDEX_TOW]
        file_month = file_parts[MappingIndex.INDEX_THREE].split(".")[MappingIndex.INDEX_ZERO]
        if file_month == month and file_year == year:
            with open(os.path.join(MappingIndex.WEATHER_DIR, file_name), "r") as file_reader:
                file_values += get_file_contents(file_reader.read())

    return file_values

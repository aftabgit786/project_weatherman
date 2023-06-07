from utils import read_files
from constant import MappingIndex


month = input('Enter month: ')
file_values = read_files(month)

for file_value in file_values:
    date = file_value[MappingIndex.date]
    sliced_date = date.split('-')[MappingIndex.sliced_date]
    maximum_temperature = file_value[MappingIndex.maximum_temperature]
    minimum_temperature = file_value[MappingIndex.minimum_temperature]

    if maximum_temperature and minimum_temperature is not None:
        print(f"{sliced_date}{int(maximum_temperature) * '+'} {maximum_temperature}C")
        print(f"{sliced_date}{int(minimum_temperature) * '+'} {minimum_temperature}C")

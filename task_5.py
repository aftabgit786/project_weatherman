from utils import read_files
from constant import MappingIndex


month = input('Enter month: ')
file_values = read_files(month)

red_code = '\033[91m'
blue_code = '\033[34m'
reset_code = '\033[0m'

for file_value in file_values:
    date = file_value[MappingIndex.date]
    sliced_date = date.split('-')[MappingIndex.sliced_date]
    maximum_temperature = file_value[MappingIndex.maximum_temperature]
    minimum_temperature = file_value[MappingIndex.minimum_temperature]

    if maximum_temperature and minimum_temperature is not None:
        print(f"{sliced_date}{blue_code}{int(minimum_temperature) * '+'}{red_code}{int(maximum_temperature) * '+'}"
              f"{reset_code} {minimum_temperature}C - {maximum_temperature}C")

import argparse
import calendar

from utils import read_files
from constants import MappingIndex


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--date', type=str, help="Date argument in the format 'year/month'")
args = parser.parse_args()

year, month_number = args.date.split(MappingIndex.SLASH)

casting = int(month_number)
month = calendar.month_abbr[casting]

file_values = read_files(month, year)

for file_value in file_values:
    date = file_value[MappingIndex.DATE]
    sliced_date = date.split('-')[MappingIndex.SLICED_DATE]
    maximum_temperature = file_value[MappingIndex.MAXIMUM_TEMPERATURE]
    minimum_temperature = file_value[MappingIndex.MINIMUM_TEMPERATURE]

    if maximum_temperature and minimum_temperature is not None:
        print(f"{sliced_date}{MappingIndex.BLUE_COLOR_CODE}{int(minimum_temperature) * '+'}"
              f"{MappingIndex.RED_COLOR_CODE}{int(maximum_temperature) * '+'}"
              f"{MappingIndex.RESET_COLOR_CODE} {minimum_temperature}C - {maximum_temperature}C")

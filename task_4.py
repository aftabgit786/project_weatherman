import argparse
import calendar

from utils import read_files
from constants import MappingIndex


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--date', type=str, help="Date argument in the format 'year/month'")
args = parser.parse_args()

year, month_number = args.date.split('/')

casting = int(month_number)
month = calendar.month_abbr[casting]

file_values = read_files(month, year)


red_code = '\033[91m'
blue_code = '\033[34m'
reset_code = '\033[0m'

for number in range(5):

    for file_value in file_values:
        date = file_value[MappingIndex.DATE]
        sliced_date = date.split('-')[MappingIndex.SLICED_DATE]
        maximum_temperature = file_value[MappingIndex.MAXIMUM_TEMPERATURE]
        minimum_temperature = file_value[MappingIndex.MINIMUM_TEMPERATURE]

        if maximum_temperature and minimum_temperature is not None:
            print(f"{sliced_date}{red_code}{int(maximum_temperature) * '+'}{reset_code} {maximum_temperature}C")
            print(f"{sliced_date}{blue_code}{int(minimum_temperature) * '+'}{reset_code} {minimum_temperature}C")

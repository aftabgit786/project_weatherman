from utils import read_files


file_values = read_files()

for file_value in file_values:
    date = file_value[0]
    sliced_date = date.split('-')[2]
    maximum_temperature = file_value[1]
    minimum_temperature = file_value[3]
    if maximum_temperature and minimum_temperature is not None:
        print(f"{sliced_date}{int(maximum_temperature) * '+'} {maximum_temperature}C")
        print(f"{sliced_date}{int(minimum_temperature) * '+'} {minimum_temperature}C")

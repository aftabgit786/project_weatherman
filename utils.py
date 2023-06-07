import os


def get_file_contents(file_content):
    file_values = []
    for row in file_content.split("\n")[1:-1]:
        file_values.append(row.split(","))
    return file_values


def read_files_for_month(month):
    file_values = []
    for file_name in os.listdir("weatherfiles"):
        if file_name.endswith(".txt"):
            file_parts = file_name.split("_")
            file_month = file_parts[3].split(".")[0]
            if file_month == month:
                with open(os.path.join("weatherfiles", file_name), "r") as file_reader:
                    file_content = file_reader.read()
                    file_values += get_file_contents(file_content)
    return file_values


def read_files_for_year(year):
    file_values = []
    for file_name in os.listdir("weatherfiles"):
        if file_name.endswith(".txt"):
            file_parts = file_name.split("_")
            file_year = file_parts[2]
            if file_year == year:
                with open(os.path.join("weatherfiles", file_name), "r") as file_reader:
                    file_content = file_reader.read()
                    file_values += get_file_contents(file_content)
    return file_values

import os


def get_file_contents(file_content):
    file_values = []
    for row in file_content.split("\n")[1:-1]:
        file_values.append(row.split(","))
    return file_values


def read_files():
    file_values = []
    for file_name in os.listdir("weatherfiles"):
        with open(f"weatherfiles/{file_name}", "r") as file_reader:
            file_content = file_reader.read()
            file_values += get_file_contents(file_content)
    return file_values

import json
import re


##### Task 1
def get_json(filename):
    with open(filename, "r") as json_file:
        read_file = json.load(json_file)
    return read_file


##### Task 2
def get_surname(item):
    full_name = item['name'].split()
    return str(full_name[len(full_name) - 1])


def sort_surname(data):
    return sorted(data, key=lambda item: get_surname(item))


##### Task 3
def get_date_death(item):
    dd = item['years'].split('–')[1]
    date_death = int("".join(re.findall(r'\d+', dd)))
    return date_death if "BC" not in dd else -date_death


def sort_date_death(data):
    return sorted(data, key=lambda item: get_date_death(item))


##### Task 4
def get_len_text(item):
    return len(item['text'].split())


def sort_len_text(data):
    return sorted(data, key=lambda item: get_len_text(item))


filename = 'data.json'
json_file = get_json(filename)

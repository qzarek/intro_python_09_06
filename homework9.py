####Task 1
def read_txt(filename):
    with open(filename, 'r') as txt_file:
        data = txt_file.readlines()
        data = [line.strip() for line in data]
    return data


def create_str_list(read_file):
    new_list = []
    for str_ in read_file:
        if "." in str_[0]:
            new_str = str_[1:]
            new_list.append(new_str)
    return new_list


# filename = "domains.txt"
# read_list = read_txt(filename)
# res = create_str_list(read_list)
# print(res)

####Task 2
def create_lastname_list(read_file):
    new_list = []
    for line in read_file:
        new_line = line.split("\t")
        if new_line[0].isdigit() and new_line[1].istitle() and len(new_line) == 4:
            new_list.append(new_line[1])
    return new_list


# filename = "names.txt"
# read_file = read_txt(filename)
# res = create_lastname_list(read_file)
# print(res)


####Task 3
def modify_date(date_line):
    new_date = ""
    parts = date_line.split()
    if len(parts) == 3:
        day = parts[0].rstrip("ndrsth")
        if len(day) == 1:
            day = f"0{day}"
        month = month_to_number(parts[1])
        if len(str(month)) == 1:
            month = f"0{month}"
        year = parts[2]
        new_date = f"{day}/{month}/{year}"
    return new_date


def get_original_dates(filename):
    new_dates = []
    data = read_txt(filename)
    for line in data:
        if " - " in line:
            new_date = line.split(" - ")[0]
            new_dates.append(new_date)
    return new_dates


def month_to_number(part):
    return ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
            "November", "December"].index(part)+1


def get_fin_list_dict(filename):
    orig_d = get_original_dates(filename)
    fin_dict_list = []
    for date in orig_d:
        date_mod = modify_date(date)
        fin_dict_list.append(dict(date_original=date, date_modified=date_mod))
    return fin_dict_list

#
# filename = "authors.txt"
# res = get_fin_list_dict(filename)
# print(res)

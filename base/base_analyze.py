import yaml


def analyze(file_name, key_name):
    with open("./data/" + file_name + ".yaml", "r") as f:
        content = yaml.load(f)

    temp_list = list()
    for temp_dict in content[key_name].values():
        temp_list.append(temp_dict)

    return temp_list

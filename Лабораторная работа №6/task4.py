import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n'):
    with open(filename) as f:
        list_ = []
        for index, line in enumerate(f):

            fields = line.strip(new_line).split(delimiter)

            if index == 0:
                heads = fields
                continue

            list_.append({})

            for i, _ in enumerate(heads):

                list_[-1][heads[i]] = fields[i]
    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

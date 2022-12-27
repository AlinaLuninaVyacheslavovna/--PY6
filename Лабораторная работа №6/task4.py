import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n'):
    with open(filename, "r") as f:
        lines = f.read().split(new_line)
        fields = lines[0].split(delimiter)
        data = [dict(zip(fields, line.split(delimiter))) for line in lines[1:]]
    return json.dumps(data, indent=4)


print(csv_to_list_dict(INPUT_FILE))

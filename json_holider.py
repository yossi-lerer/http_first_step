import json

def write_json(data):
    if type(data) != list:
        data = [data]
    json_str = json.dumps(data, indent=4)
    with open("data.json", "w") as f:
        f.write(json_str)

def get_json():
    with open("data.json", "r") as file:
        data = json.load(file)
    if data == []:
        return False
    return data


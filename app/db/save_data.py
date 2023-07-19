import json


def save_data(data):
    filename = "./db/phrases.json"
    with open(filename, "r") as read_file:
        treatedJson = json.load(read_file)
        treatedJson.update(data)
        jsonData = json.dumps(treatedJson, indent=4)
        with open(filename, "w") as write_file:
            write_file.write(jsonData)

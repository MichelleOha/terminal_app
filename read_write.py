import json

# this class will read and write to a json file (store data)


class ReadWrite:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_json_list(self):
        input_file = open(self.file_path)
        json_list = json.load(input_file)
        return json_list

    def write_item_to_json(self, item):
        input_file = open(self.file_path)
        json_list = json.load(input_file)
        json_list.append(item)
        with open(self.file_path, 'w') as my_file:
            json.dump(json_list, my_file)

    def write_list_to_json(self, list):
        with open(self.file_path, 'w') as my_file:
            json.dump(list, my_file)

    def reset_json(self):
        with open(self.file_path, 'w') as my_file:
            json.dump([], my_file)

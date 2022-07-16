import json

# This class will read and write to a json file (store data)s


class ReadWrite:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_json_list(self):
        try:
            input_file = open(self.file_path)
            json_list = json.load(input_file)
            return json_list
        except:
            raise IOError(
                "There was an issue reading your list.json file. Please make sure it exists and is in the correct format.")

    def write_item_to_json(self, item):
        try:
            input_file = open(self.file_path)
            json_list = json.load(input_file)
            json_list.append(item)
            with open(self.file_path, 'w') as my_file:
                json.dump(json_list, my_file)
        except:
            raise IOError(
                "There was an issue reading your list.json file. Please make sure it exists and is in the correct format.")

    def write_list_to_json(self, list):
        try:
            with open(self.file_path, 'w') as my_file:
                json.dump(list, my_file)
        except:
            raise IOError(
                "There was an issue reading your list.json file. Please make sure it exists and is in the correct format.")

    def reset_json(self):
        try:
            with open(self.file_path, 'w') as my_file:
                json.dump([], my_file)
        except:
            raise IOError(
                "There was an issue reading your list.json file. Please make sure it exists and is in the correct format.")

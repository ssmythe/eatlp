import json


class User:
    """
    User is used to store a details about a user
    """

    def __init__(self):
        self.dict_of_user = {}

    def len(self):
        return len(self.dict_of_user)

    def read_user_from_json_file(self, json_file):
        with open(json_file, 'r') as file:
            self.dict_of_user = json.load(file)

    def write_user_to_json_file(self, json_file):
        with open(json_file, 'w') as file:
            json.dump(self.dict_of_user, file, sort_keys=True, indent=4)

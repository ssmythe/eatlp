from src.item import Item
import json


class Items:
    """
    Items is used to contain multiple Item objects
    """

    def __init__(self):
        self.list_of_items = []

    def len(self):
        return len(self.list_of_items)

    def add_item(self, item):
        self.list_of_items.append(item)

    def list_of_items_names(self):
        rc_list = []
        for item in self.list_of_items:
            rc_list.append(item.name)
        return sorted(rc_list)

    def add_items_from_json_file(self, json_file):
        with open(json_file, 'r') as file:
            json_dict = json.load(file)

        for jdk, jdv in json_dict.items():
            jd_item_dict = {
                jdk: jdv
            }
            item = Item()
            json_str = json.dumps(jd_item_dict, indent=4)
            item.set_item_from_json_str(json_str)
            self.add_item(item)

    def get_item_from_items_by_name(self, name):
        for item in self.list_of_items:
            if item.name == name:
                return item
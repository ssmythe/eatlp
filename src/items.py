from src.item import Item
import json


# TODO refactor list_of_items to be dict_of_items

class Items:
    """
    Items is used to contain multiple Item objects
    """

    def __init__(self):
        self.dict_of_items = {}

    def len(self):
        return len(self.dict_of_items)

    def add_name_item(self, name, item):
        self.dict_of_items[name] = item

    def list_of_items_names(self):
        return sorted(self.dict_of_items.keys())

    def add_items_from_json_file(self, json_file):
        with open(json_file, 'r') as file:
            json_dict = json.load(file)

        for name, jdv in json_dict.items():
            jd_item_dict = {
                name: jdv
            }
            item = Item()
            json_str = json.dumps(jd_item_dict, indent=4)
            item.set_item_from_json_str(json_str)
            self.add_name_item(name, item)

    def get_item_from_items_by_name(self, name):
        return self.dict_of_items[name]
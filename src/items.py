from src.item import Item
import json


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

    def write_items_to_json_file(self, json_file):
        expanded_dict_of_items = {}
        for name, item in self.dict_of_items.items():
            fixed_item = {}
            for k, v in item.dict_of_item.items():
                spaced_key = k.replace('_per_serving', '').replace('_', ' ')
                fixed_item[spaced_key] = v
            expanded_dict_of_items[name] = fixed_item

        with open(json_file, 'w') as file:
            json.dump(expanded_dict_of_items, file, sort_keys=True, indent=4)

    def get_item_from_items_by_name(self, name):
        return self.dict_of_items[name]

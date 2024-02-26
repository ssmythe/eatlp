import json


class Item:
    """
    Item is for store bought products
    """

    def __init__(self):
        self.dict_of_item = {}

    def set_name(self, name):
        self.name = name
        # self.dict_of_item['name'] = name

    def set_store_product_name(self, store_product_name):
        self.store_product_name = store_product_name
        self.dict_of_item['store_product_name'] = store_product_name

    def set_store(self, store):
        self.store = store
        self.dict_of_item['store'] = store

    def set_price(self, price):
        self.price = price
        self.dict_of_item['price'] = price

    def set_servings_per_container(self, servings_per_container):
        self.servings_per_container = servings_per_container
        self.dict_of_item['servings_per_container'] = servings_per_container

    def set_serving_size(self, serving_size):
        self.serving_size = serving_size
        self.dict_of_item['serving_size'] = serving_size

    def set_carb_per_serving(self, carb_per_serving):
        self.carb_per_serving = carb_per_serving
        self.dict_of_item['carb_per_serving'] = carb_per_serving

    def set_fat_per_serving(self, fat_per_serving):
        self.fat_per_serving = fat_per_serving
        self.dict_of_item['fat_per_serving'] = fat_per_serving

    def set_fiber_per_serving(self, fiber_per_serving):
        self.fiber_per_serving = fiber_per_serving
        self.dict_of_item['fiber_per_serving'] = fiber_per_serving

    def set_protein_per_serving(self, protein_per_serving):
        self.protein_per_serving = protein_per_serving
        self.dict_of_item['protein_per_serving'] = protein_per_serving

    def set_sodium_per_serving(self, sodium_per_serving):
        self.sodium_per_serving = sodium_per_serving
        self.dict_of_item['sodium_per_serving'] = sodium_per_serving

    def price_per_serving(self):
        return round(self.price / self.servings_per_container, 2)  # round okay

    def kcal_per_serving(self):
        kcal_carb = self.carb_per_serving * 4
        kcal_fat = self.fat_per_serving * 9
        kcal_protein = self.protein_per_serving * 4
        return kcal_carb + kcal_fat + kcal_protein

    def set_item_from_dict(self, data):
        self.set_name(data['name'])
        self.set_store(data['store'])
        self.set_store_product_name(data['store_product_name'])
        self.set_price(data['price'])
        self.set_servings_per_container(data['servings_per_container'])
        self.set_serving_size(data['serving_size'])
        self.set_carb_per_serving(data['carb_per_serving'])
        self.set_fat_per_serving(data['fat_per_serving'])
        self.set_fiber_per_serving(data['fiber_per_serving'])
        self.set_protein_per_serving(data['protein_per_serving'])
        self.set_sodium_per_serving(data['sodium_per_serving'])

    def set_item_from_json_str(self, json_str):
        json_dict = json.loads(json_str)
        data_dict = {}
        name = list(json_dict.keys())[0]
        data_dict['name'] = name
        data_dict['price'] = json_dict[name]['price']
        data_dict['store'] = json_dict[name]['store']
        data_dict['store_product_name'] = json_dict[name]['store product name']
        data_dict['servings_per_container'] = (
            json_dict[name]['servings per container']
        )
        data_dict['serving_size'] = json_dict[name]['serving size']
        data_dict['carb_per_serving'] = json_dict[name]['carb']
        data_dict['fat_per_serving'] = json_dict[name]['fat']
        data_dict['fiber_per_serving'] = json_dict[name]['fiber']
        data_dict['protein_per_serving'] = json_dict[name]['protein']
        data_dict['sodium_per_serving'] = json_dict[name]['sodium']
        self.set_item_from_dict(data_dict)

    def set_item_from_json_file(self, json_file):
        with open(json_file, 'r') as file:
            json_str = json.dumps(json.load(file), indent=4)
        self.set_item_from_json_str(json_str)

import json


class Recipe:
    """
    Recipe is for collections of store bought products in servings
    """

    def __init__(self):
        self.ingredients = {}

    def set_name(self, name):
        self.name = name

    def set_servings_per_recipe(self, servings_per_recipe):
        self.servings_per_recipe = servings_per_recipe

    def set_serving_size(self, serving_size):
        self.serving_size = serving_size

    def set_ingredients(self, ingredients):
        self.ingredients = ingredients

    def set_recipe_from_dict(self, data):
        self.set_name(data['name'])
        self.set_servings_per_recipe(data['servings_per_recipe'])
        self.set_serving_size(data['serving_size'])
        self.set_ingredients(data['ingredients'])

    def set_recipe_from_json_str(self, json_str):
        json_dict = json.loads(json_str)
        data_dict = {}
        name = list(json_dict.keys())[0]
        data_dict['name'] = name
        data_dict['servings_per_recipe'] = json_dict[name]['servings per recipe']
        data_dict['serving_size'] = json_dict[name]['serving size']
        data_dict['ingredients'] = json_dict[name]['ingredients']
        self.set_recipe_from_dict(data_dict)

    def set_recipe_from_json_file(self, json_file):
        with open(json_file, 'r') as file:
            json_str = json.dumps(json.load(file), indent=4)
        self.set_recipe_from_json_str(json_str)

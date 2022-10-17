from src.recipe import Recipe

import json


class Recipes:
    """
    Recipes is used to contain multiple Recipe objects
    """

    def __init__(self):
        self.dict_of_recipes = {}

    def len(self):
        return len(self.dict_of_recipes)

    def add_name_item(self, name, recipe):
        self.dict_of_recipes[name] = recipe

    def list_of_recipes_names(self):
        return sorted(self.dict_of_recipes.keys())

    def add_recipes_from_json_file(self, json_file):
        with open(json_file, 'r') as file:
            json_dict = json.load(file)

        for name, jdv in json_dict.items():
            jd_item_dict = {
                name: jdv
            }
            recipe = Recipe()
            json_str = json.dumps(jd_item_dict, indent=4)
            recipe.set_recipe_from_json_str(json_str)
            self.add_name_item(name, recipe)

    def get_recipe_from_recipes_by_name(self, name):
        return self.dict_of_recipes[name]

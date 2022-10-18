from src.food import Food

import json


class Foods:
    """
    Foods is used to contain multiple Food objects with calculated values
    """

    def __init__(self):
        self.dict_of_foods = {}

    def len(self):
        return len(self.dict_of_foods)

    def add_name_food(self, name, food):
        self.dict_of_foods[name] = food.dict_of_food

    def recipes_to_foods(self, items, recipes):
        for recipe_name in recipes.list_of_recipes_names():
            recipe = recipes.get_recipe_from_recipes_by_name(recipe_name)
            food = Food()
            food.recipe_to_food(items, recipe)
            self.add_name_food(recipe_name, food)

    def foods_to_json_str(self):
        return json.dumps(self.dict_of_foods, sort_keys=True, indent=4)

    def write_foods_to_json_file(self, json_file):
        with open(json_file, 'w') as file:
            json.dump(self.dict_of_foods, file, sort_keys=True, indent=4)

    def read_foods_from_json_file(self, json_file):
        with open(json_file, 'r') as file:
            self.dict_of_foods = json.load(file)

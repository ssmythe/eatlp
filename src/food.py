from src.recipe import Recipe

import json


class Food:
    """
    Food is used to store a single food object with calculated values per serving
    """

    def __init__(self):
        pass

    def set_name(self, name):
        self.name = name

    def set_servings_per_food(self, servings_per_food):
        self.servings_per_food = servings_per_food

    def set_serving_size(self, serving_size):
        self.serving_size = serving_size

    def set_min_servings(self, min_servings):
        self.min_servings = min_servings

    def set_max_servings(self, max_servings):
        self.max_servings = max_servings

    def recipe_to_food(self, recipe, food):
        self.set_name(recipe.name)
        self.set_servings_per_food(recipe.servings_per_recipe)
        self.set_serving_size(recipe.serving_size)
        self.set_min_servings(recipe.min_servings)
        self.set_max_servings(recipe.max_servings)
        
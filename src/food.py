from src.recipe import Recipe
from src.items import Items

import json


class Food:
    """
    Food is used to store a single food object with calculated values per serving
    """

    def __init__(self):
        self.dict_of_food = {}

    def set_name(self, name):
        self.name = name

    def set_servings_per_food(self, servings_per_food):
        self.servings_per_food = servings_per_food
        self.dict_of_food['servings_per_food'] = servings_per_food

    def set_serving_size(self, serving_size):
        self.serving_size = serving_size
        self.dict_of_food['serving_size'] = serving_size

    def set_min_servings(self, min_servings):
        self.min_servings = min_servings
        self.dict_of_food['min_servings'] = min_servings

    def set_max_servings(self, max_servings):
        self.max_servings = max_servings
        self.dict_of_food['max_servings'] = max_servings

    def set_carb_per_serving(self, carb_per_serving):
        self.carb_per_serving = carb_per_serving
        self.dict_of_food['carb_per_serving'] = carb_per_serving

    def set_fat_per_serving(self, fat_per_serving):
        self.fat_per_serving = fat_per_serving
        self.dict_of_food['fat_per_serving'] = fat_per_serving

    def set_protein_per_serving(self, protein_per_serving):
        self.protein_per_serving = protein_per_serving
        self.dict_of_food['protein_per_serving'] = protein_per_serving

    def set_sodium_per_serving(self, sodium_per_serving):
        self.sodium_per_serving = sodium_per_serving
        self.dict_of_food['sodium_per_serving'] = sodium_per_serving

    def set_kcal_per_serving(self, kcal_per_serving):
        self.kcal_per_serving = kcal_per_serving
        self.dict_of_food['kcal_per_serving'] = kcal_per_serving

    def set_price_per_serving(self, price_per_serving):
        self.price_per_serving = price_per_serving
        self.dict_of_food['price_per_serving'] = price_per_serving

    def recipe_to_food(self, items, recipe):
        self.set_name(recipe.name)
        self.set_servings_per_food(recipe.servings_per_recipe)
        self.set_serving_size(recipe.serving_size)
        self.set_min_servings(recipe.min_servings)
        self.set_max_servings(recipe.max_servings)
        self.set_carb_per_serving(recipe.total_carb_per_recipe_serving(items))
        self.set_fat_per_serving(recipe.total_fat_per_recipe_serving(items))
        self.set_protein_per_serving(
            recipe.total_protein_per_recipe_serving(items))
        self.set_sodium_per_serving(
            recipe.total_sodium_per_recipe_serving(items))
        self.set_kcal_per_serving(recipe.total_kcal_per_recipe_serving(items))
        self.set_price_per_serving(
            recipe.total_price_per_recipe_serving(items))

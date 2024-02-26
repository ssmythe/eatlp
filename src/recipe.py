import json


class Recipe:
    """
    Recipe is for collections of store bought products in servings
    """

    def __init__(self):
        self.ingredients = {}
        self.dict_of_recipe = {}

    def set_name(self, name):
        self.name = name

    def set_servings_per_recipe(self, servings_per_recipe):
        self.servings_per_recipe = servings_per_recipe
        self.dict_of_recipe['servings_per_recipe'] = servings_per_recipe

    def set_serving_size(self, serving_size):
        self.serving_size = serving_size
        self.dict_of_recipe['serving_size'] = serving_size

    def set_ingredients(self, ingredients):
        self.ingredients = ingredients
        ingredients_dict = {}
        for k, v in ingredients.items():
            ingredients_dict[k] = v
        self.dict_of_recipe['ingredients'] = ingredients_dict

    def set_min_servings(self, min_servings):
        self.min_servings = min_servings
        self.dict_of_recipe['min_servings'] = min_servings

    def set_max_servings(self, max_servings):
        self.max_servings = max_servings
        self.dict_of_recipe['max_servings'] = max_servings

    def set_recipe_from_dict(self, data):
        self.set_name(data['name'])
        self.set_servings_per_recipe(data['servings_per_recipe'])
        self.set_serving_size(data['serving_size'])
        self.set_ingredients(data['ingredients'])
        self.set_min_servings(data['min_servings'])
        self.set_max_servings(data['max_servings'])

    def set_recipe_from_json_str(self, json_str):
        json_dict = json.loads(json_str)
        data_dict = {}
        name = list(json_dict.keys())[0]
        data_dict['name'] = name
        data_dict['servings_per_recipe'] = (
            json_dict[name]['servings per recipe']
        )
        data_dict['serving_size'] = json_dict[name]['serving size']
        data_dict['ingredients'] = json_dict[name]['ingredients']
        data_dict['min_servings'] = json_dict[name]['min_servings']
        data_dict['max_servings'] = json_dict[name]['max_servings']
        self.set_recipe_from_dict(data_dict)

    def set_recipe_from_json_file(self, json_file):
        with open(json_file, 'r') as file:
            json_str = json.dumps(json.load(file), indent=4)
        self.set_recipe_from_json_str(json_str)

    def carb_per_ingredient_to_list(self, items):
        carb_list = []
        for ingredient, qty in self.ingredients.items():
            item = items.get_item_from_items_by_name(ingredient)
            carb_list.append(item.carb_per_serving *
                             qty / self.servings_per_recipe)
        return carb_list

    def total_carb_per_recipe_serving(self, items):
        total_carb = 0
        for carb in self.carb_per_ingredient_to_list(items):
            total_carb += carb
        return total_carb

    def fat_per_ingredient_to_list(self, items):
        fat_list = []
        for ingredient, qty in self.ingredients.items():
            item = items.get_item_from_items_by_name(ingredient)
            fat_list.append(item.fat_per_serving * qty /
                            self.servings_per_recipe)
        return fat_list

    def total_fat_per_recipe_serving(self, items):
        total_fat = 0
        for fat in self.fat_per_ingredient_to_list(items):
            total_fat += fat
        return total_fat

    def fiber_per_ingredient_to_list(self, items):
        fiber_list = []
        for ingredient, qty in self.ingredients.items():
            item = items.get_item_from_items_by_name(ingredient)
            fiber_list.append(item.fiber_per_serving *
                              qty / self.servings_per_recipe)
        return fiber_list

    def total_fiber_per_recipe_serving(self, items):
        total_fiber = 0
        for fiber in self.fiber_per_ingredient_to_list(items):
            total_fiber += fiber
        return total_fiber

    def protein_per_ingredient_to_list(self, items):
        protein_list = []
        for ingredient, qty in self.ingredients.items():
            item = items.get_item_from_items_by_name(ingredient)
            protein_list.append(item.protein_per_serving *
                                qty / self.servings_per_recipe)
        return protein_list

    def total_protein_per_recipe_serving(self, items):
        total_protein = 0
        for protein in self.protein_per_ingredient_to_list(items):
            total_protein += protein
        return total_protein

    def sodium_per_ingredient_to_list(self, items):
        sodium_list = []
        for ingredient, qty in self.ingredients.items():
            item = items.get_item_from_items_by_name(ingredient)
            sodium_list.append(item.sodium_per_serving *
                               qty / self.servings_per_recipe)
        return sodium_list

    def total_sodium_per_recipe_serving(self, items):
        total_sodium = 0
        for sodium in self.sodium_per_ingredient_to_list(items):
            total_sodium += sodium
        return total_sodium

    def kcal_per_ingredient_to_list(self, items):
        kcal_list = []
        for ingredient, qty in self.ingredients.items():
            item = items.get_item_from_items_by_name(ingredient)
            kcal_list.append(item.kcal_per_serving() *
                             qty / self.servings_per_recipe)
        return kcal_list

    def total_kcal_per_recipe_serving(self, items):
        total_kcal = 0
        for kcal in self.kcal_per_ingredient_to_list(items):
            total_kcal += kcal
        return total_kcal

    def price_per_ingredient_to_list(self, items):
        price_list = []
        for ingredient, qty in self.ingredients.items():
            item = items.get_item_from_items_by_name(ingredient)
            price_list.append(round(item.price_per_serving(
            ) * qty / self.servings_per_recipe, 2))  # round okay
        return price_list

    def total_price_per_recipe_serving(self, items):
        total_price = 0
        for price in self.price_per_ingredient_to_list(items):
            total_price += price
        return round(total_price, 2)  # round okay

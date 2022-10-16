class Item:
    """
    Item is for store bought products
    """

    def __init__(self):
        pass

    def set_name(self, name):
        self.name = name

    def set_brand_name(self, brand_name):
        self.brand_name = brand_name

    def set_price(self, price):
        self.price = price

    def set_servings_per_container(self, servings_per_container):
        self.servings_per_container = servings_per_container

    def set_serving_size(self, serving_size):
        self.serving_size = serving_size

    def set_kcal_per_serving(self, kcal_per_serving):
        self.kcal_per_serving = kcal_per_serving

    def set_carb_per_serving(self, carb_per_serving):
        self.carb_per_serving = carb_per_serving

    def set_fat_per_serving(self, fat_per_serving):
        self.fat_per_serving = fat_per_serving

    def set_protein_per_serving(self, protein_per_serving):
        self.protein_per_serving = protein_per_serving

    def set_sodium_per_serving(self, sodium_per_serving):
        self.sodium_per_serving = sodium_per_serving

    def cost_per_serving(self):
        return round(self.price / self.servings_per_container, 2)

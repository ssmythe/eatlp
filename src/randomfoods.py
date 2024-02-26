import random


class RandomFoods:
    """
    RandomFoods is used to contain multiple Food objects with calculated
    values selected as a random subset of Foods
    """

    def __init__(self):
        self.dict_of_random_foods = {}

    def len(self):
        return len(self.dict_of_random_foods)

    def foods_to_randomfoods(self, foods, num_of_random_foods,
                             set_random_seed=None):
        for food in foods.dict_of_foods.keys():
            if foods.dict_of_foods[food]['min_servings'] > 0:
                self.dict_of_random_foods[food] = foods.dict_of_foods[food]
        if set_random_seed is not None:
            random.seed(set_random_seed)
        list_of_randomly_selected_foods = random.sample(
            tuple(foods.dict_of_foods.keys()), num_of_random_foods)
        for food in list_of_randomly_selected_foods:
            self.dict_of_random_foods[food] = foods.dict_of_foods[food]

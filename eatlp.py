#!/usr/bin/env python3

# TODO save results of food dict and solution
# TODO consider added sugars constraints
# TODO figure out menus
# TODO conditional logic on recommended protein for over 40 years old 1.0-1.2 g/kg body weight per day
# TODO Script to populate user.json to keep track of user details like age height weight weight loss preference
#      Update current weight, target weight…

from multiprocessing import current_process
from src.bmi import *
from src.foods import *
from src.food import *
from src.randomfoods import *
from pulp import *
import random


# Model return status codes:
# LpStatus key          string value   numerical value
# LpStatusOptimal 	  “Optimal”       1
# LpStatusNotSolved 	  “Not Solved”    0
# LpStatusInfeasible 	  “Infeasible”   -1
# LpStatusUnbounded 	  “Unbounded”    -2
# LpStatusUndefined 	  “Undefined”    -3
model_return_status_codes = {
    
    '1': 'Optimal',
    '0': 'Not Solved',
    '-1': 'Infeasible',
    '-2': 'Unbounded',
    '-3': 'Undefined'
}
global status

current_weight_lbs = 268.8
max_kcal = 1643
max_sodium = 2000

# recommended protein
# KgPerPound 0.453592
# =CurrentWeight*KgPerPound*0.8
minimum_recommended_protein = BMI.lbs_to_kg(current_weight_lbs) * 0.8
# print(f"minimum recommended protein #1 : {minimum_recommended_protein}")
# minimum_recommended_protein = current_weight_lbs * 0.36
# print(f"recommended protein #2: {minimum_recommended_protein}")

plus_minus_percent = 0.05
carb_percent = 0.50
fat_percent = 0.30
protein_percent = 0.20
min_carb = max_kcal * (carb_percent - plus_minus_percent) / 4
max_carb = max_kcal * (carb_percent + plus_minus_percent) / 4
min_fat = max_kcal * (fat_percent - plus_minus_percent) / 9
max_fat = max_kcal * (fat_percent + plus_minus_percent) / 9
min_protein = max_kcal * (protein_percent - plus_minus_percent) / 4
max_protein = max_kcal * (protein_percent - plus_minus_percent) / 4

# print(f"carb {min_carb}-{max_carb}    fat {min_fat}-{max_fat}    protein {min_protein}-{max_protein}    ")

foods = Foods()
foods.read_foods_from_json_file('data/foods.json')

loop_max = 100
for loop_counter in range(0, loop_max + 1):
    randomfoods = RandomFoods()
    choice = random.randint(1, foods.len())
    randomfoods.foods_to_randomfoods(foods, choice)
    list_of_sorted_foods = sorted(randomfoods.dict_of_random_foods.keys())

    # Define model - naming the maximine model
    model = LpProblem('eat2', LpMaximize)

    # Define variables - name, lower bound, upper bound, category Integer
    i = 1
    for name in list_of_sorted_foods:
        varname = f'x{i}'
        expr = LpVariable(name, 0, None, cat='Integer')
        globals()[varname] = expr
        i += 1

    # Define objective - max kcals
    expr = ''
    i = 1
    for name in list_of_sorted_foods:
        key = f'x{i}'
        food = foods.dict_of_foods[name]
        expr += f"{food['kcal_per_serving']}*{key} +"
        i += 1
    expr += "0"
    globals()['model'] += eval(expr)

    # Define constraints
    # min_servings
    key_str = 'model'
    i = 1
    for name in list_of_sorted_foods:
        key = f'x{i}'
        expr = ''
        food = foods.dict_of_foods[name]
        expr += f"{key} >= {food['min_servings']}"
        globals()['model'] += eval(expr)
        i += 1

    # max_servings
    key_str = 'model'
    i = 1
    for name in list_of_sorted_foods:
        key = f'x{i}'
        expr = ''
        food = foods.dict_of_foods[name]
        expr += f"{key} <= {food['max_servings']}"
        globals()['model'] += eval(expr)
        i += 1

    # max_kcal
    expr = ''
    i = 1
    for name in list_of_sorted_foods:
        key = f'x{i}'
        food = foods.dict_of_foods[name]
        expr += f"{food['kcal_per_serving']}*{key} +"
        i += 1
    expr += "0 <= {max_kcal}"
    globals()['model'] += eval(expr)

    # max_sodium
    expr = ''
    i = 1
    for name in list_of_sorted_foods:
        key = f'x{i}'
        food = foods.dict_of_foods[name]
        expr += f"{food['sodium_per_serving']}*{key} + "
        i += 1
    expr += "0 <= {max_sodium}"
    globals()['model'] += eval(expr)

    # min_carb
    expr = ''
    i = 1
    for name in list_of_sorted_foods:
        key = f'x{i}'
        food = foods.dict_of_foods[name]
        expr += f"{food['carb_per_serving']}*{key} +"
        i += 1
    expr += "0 >= {min_carb}"
    globals()['model'] += eval(expr)

    # max_carb
    expr = ''
    i = 1
    for name in list_of_sorted_foods:
        key = f'x{i}'
        food = foods.dict_of_foods[name]
        expr += f"{food['carb_per_serving']}*{key} +"
        i += 1
    expr += "0 <= {max_carb}"
    globals()['model'] += eval(expr)

    # min_fat
    expr = ''
    i = 1
    for name in list_of_sorted_foods:
        key = f'x{i}'
        food = foods.dict_of_foods[name]
        expr += f"{food['fat_per_serving']}*{key} +"
        i += 1
    expr += "0 >= {min_fat}"
    globals()['model'] += eval(expr)

    # max_fat
    expr = ''
    i = 1
    for name in list_of_sorted_foods:
        key = f'x{i}'
        food = foods.dict_of_foods[name]
        expr += f"{food['fat_per_serving']}*{key} +"
        i += 1
    expr += "0 <= {max_fat}"
    globals()['model'] += eval(expr)

    # # min_protein
    # expr = ''
    # i = 1
    # for name in list_of_sorted_foods:
    #     key = f'x{i}'
    #     food = foods.dict_of_foods[name]
    #     expr += f"{food['protein_per_serving']}*{key} +"
    #     i += 1
    # expr += "0 >= {min_protein}"
    # globals()['model'] += eval(expr)

    # # max_protein
    # expr = ''
    # i = 1
    # for name in list_of_sorted_foods:
    #     key = f'x{i}'
    #     food = foods.dict_of_foods[name]
    #     expr += f"{food['protein_per_serving']}*{key} +"
    #     i += 1
    # expr += "0 <= {max_protein}"
    # globals()['model'] += eval(expr)

    # minimum recommended protein
    expr = ''
    i = 1
    for name in list_of_sorted_foods:
        key = f'x{i}'
        food = foods.dict_of_foods[name]
        expr += f"{food['protein_per_serving']}*{key} +"
        i += 1
    expr += "0 >= {minimum_recommended_protein}"
    globals()['model'] += eval(expr)

    # Solve problem
    status = model.solve(PULP_CBC_CMD(msg=False))
    if status == 1:
        break

print(f"Model: {model_return_status_codes[str(status)]}")
# Print model
# print(model)

# Print the variables optimized value
print(98 * '-')
total_kcal = 0
total_carb = 0
total_fat = 0
total_protein = 0
total_sodium = 0
total_price = 0
for v in model.variables():
    name = v.name.replace('_', ' ')
    food = foods.dict_of_foods[name]
    kcal = food['kcal_per_serving']
    kcal_times_servings = kcal * v.varValue
    carb = food['carb_per_serving']
    carb_times_servings = carb * v.varValue
    fat = food['fat_per_serving']
    fat_times_servings = fat * v.varValue
    protein = food['protein_per_serving']
    protein_times_servings = protein * v.varValue
    sodium = food['sodium_per_serving']
    sodium_times_servings = sodium * v.varValue
    price = food['price_per_serving']
    price_times_servings = price * v.varValue
    total_kcal += kcal_times_servings
    total_carb += carb_times_servings
    total_fat += fat_times_servings
    total_protein += protein_times_servings
    total_sodium += sodium_times_servings
    total_price += price_times_servings
    if v.varValue > 0:
        print("%dx %-30s kcal %4d, carb %4d, fat %3d, protein %3d, sodium %4d, $%6.2f" %
              (v.varValue, name, kcal_times_servings, carb_times_servings, fat_times_servings, protein_times_servings, sodium_times_servings, price_times_servings))

carb_percent = (total_carb * 4 / total_kcal) * 100
fat_percent = (total_fat * 9 / total_kcal) * 100
protein_percent = (total_protein * 4 / total_kcal) * 100

print(98 * '-')
print("%-33s kcal %4d, carb %4d, fat %3d, protein %3d, sodium %4d, $%6.2f" %
      ("Totals:", total_kcal, total_carb, total_fat, total_protein, total_sodium, total_price))
print("%-33s %4.1f%% carb / %4.1f%% fat / %4.1f%% protein" %
      ("Nutrients:", carb_percent, fat_percent, protein_percent))
print()
for v in model.variables():
    name = v.name.replace('_', ' ')
    servings = int(v.varValue)
    if servings > 0:
        for i in range(1, servings + 1):
            print("[ ] %s" % (name))


# The optimised objective function value is printed to the screen
# print('Value of Objective Function =', value(model.objective))

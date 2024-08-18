#!/usr/bin/env python

from src.bmi import BMI
from src.foods import Foods
from src.randomfoods import RandomFoods
from src.user import User
from src.msje import MSJE
from pulp import LpProblem, LpMinimize, LpVariable, PULP_CBC_CMD
import random
import pytest


pytestmark = pytest.mark.skip

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


user = User()
user.read_user_from_json_file('user.json')
target_weight_lbs = BMI.height_inches_bmi_to_weight_lbs(
    user.dict_of_user['height_inches'], user.dict_of_user['target_bmi'])
# Assigning intermediate results to variables
user_target_kcal = MSJE.target_kcal_user_target_weight_lbs(
    user, target_weight_lbs
)
kcal_adjustment = user.dict_of_user['kcal_adjust']

# Combining the results in a separate line
max_kcal = user_target_kcal + kcal_adjustment
current_weight_lbs = user.dict_of_user['current_weight_lbs']
current_age = user.dict_of_user['current_age']
min_sodium = user.dict_of_user['min_sodium']
max_sodium = user.dict_of_user['max_sodium']
max_num_of_menus = user.dict_of_user['max_num_of_menus']
data_dir = user.dict_of_user['data_dir']

# ----
# carb
# ----
min_carb_percent = 0.45
max_carb_percent = 0.65
min_carb = max_kcal * min_carb_percent / 4
max_carb = max_kcal * max_carb_percent / 4

# ---
# fat
# ---
min_fat_percent = 0.20
max_fat_percent = 0.35
min_fat = max_kcal * min_fat_percent / 9
max_fat = max_kcal * max_fat_percent / 9

# -------
# fiber
# -------
# USDA’s recommended daily amount for adults up to age 50 is 25 grams for
# women and 38 grams for men.
#
# Women and men older than 50 should have 21 and 30 daily grams, respectively.
if current_age <= 50:
    minimum_recommended_fiber = 25
else:
    # for 50 or older, recommendeded fiber 21
    minimum_recommended_fiber = 21

# On the other hand, eating too much fiber can cause bloating, gas, and
# constipation.  These adverse effects may appear after eating 70 g of
# fiber in a day.
maximum_recommended_fiber = 70

# -------
# protein
# -------
# if current_age < 40:
#     # for under 40, recommendeded protein = CurrentWeight*KgPerPound*0.8
#     minimum_recommended_protein = BMI.lbs_to_kg(current_weight_lbs) * 0.8
# else:
#     # for 40 or older, recommendeded protein (to prevent sarcopenia) =
#       CurrentWeight*KgPerPound*(1.0-1.2g/kg)
#     minimum_recommended_protein = BMI.lbs_to_kg(current_weight_lbs) * 1.0
#
# maximum_recommended_protein = BMI.lbs_to_kg(current_weight_lbs) * 2.0

min_protein_percent = 0.10
max_protein_percent = 0.35
minimum_recommended_protein = max_kcal * min_fat_percent / 4
maximum_recommended_protein = max_kcal * max_fat_percent / 4

foods = Foods()
foods.read_foods_from_json_file(data_dir + '/foods.json')

dict_of_menus = {}
menu_num = 0

for menu_count in range(1, max_num_of_menus + 1):
    loop_max = 100
    for loop_counter in range(0, loop_max + 1):
        randomfoods = RandomFoods()
        choice = random.randint(1, foods.len())
        randomfoods.foods_to_randomfoods(foods, choice)
        list_of_sorted_foods = sorted(randomfoods.dict_of_random_foods.keys())

        # Define model - naming the minimize model
        model = LpProblem('eat2', LpMinimize)

        # Define variables - name, lower bound, upper bound, category Integer
        i = 1
        for name in list_of_sorted_foods:
            varname = f'x{i}'
            expr = LpVariable(name, 0, None, cat='Integer')
            globals()[varname] = expr
            i += 1

        # Define objective - min price
        expr = ''
        i = 1
        for name in list_of_sorted_foods:
            key = f'x{i}'
            food = foods.dict_of_foods[name]
            expr += f"{food['price_per_serving']}*{key} +"
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

        # min_sodium
        expr = ''
        i = 1
        for name in list_of_sorted_foods:
            key = f'x{i}'
            food = foods.dict_of_foods[name]
            expr += f"{food['sodium_per_serving']}*{key} + "
            i += 1
        expr += "0 >= {min_sodium} "
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

        # ----
        # carb
        # ----
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

        # ---
        # fat
        # ---
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

        # fiber
        # minimum recommended fiber
        expr = ''
        i = 1
        for name in list_of_sorted_foods:
            key = f'x{i}'
            food = foods.dict_of_foods[name]
            expr += f"{food['fiber_per_serving']}*{key} +"
            i += 1
        expr += "0 >= {minimum_recommended_fiber}"
        globals()['model'] += eval(expr)

        # maximum recommended fiber
        expr = ''
        i = 1
        for name in list_of_sorted_foods:
            key = f'x{i}'
            food = foods.dict_of_foods[name]
            expr += f"{food['fiber_per_serving']}*{key} +"
            i += 1
        expr += "0 <= {maximum_recommended_fiber}"
        globals()['model'] += eval(expr)

        # protein
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

        # maximum recommended protein
        expr = ''
        i = 1
        for name in list_of_sorted_foods:
            key = f'x{i}'
            food = foods.dict_of_foods[name]
            expr += f"{food['protein_per_serving']}*{key} +"
            i += 1
        expr += "0 <= {maximum_recommended_protein}"
        globals()['model'] += eval(expr)

        # Solve problem
        status = model.solve(PULP_CBC_CMD(msg=False))
        if status == 1:
            break

    if status < 1:
        continue

    menu_str = ''
    menu_found_flag = 0

    for v in model.variables():
        name = v.name.replace('_', ' ')
        food = foods.dict_of_foods[name]
        kcal = food['kcal_per_serving']
        kcal_times_servings = kcal * v.varValue
        carb = food['carb_per_serving']
        carb_times_servings = carb * v.varValue
        fat = food['fat_per_serving']
        fat_times_servings = fat * v.varValue
        fiber = food['fiber_per_serving']
        fiber_times_servings = fiber * v.varValue
        protein = food['protein_per_serving']
        protein_times_servings = protein * v.varValue
        sodium = food['sodium_per_serving']
        sodium_times_servings = sodium * v.varValue

        if v.varValue > 0:
            menu_str += ("%dx %-30s kcal %4d, carb %4d, fat %3d, "
                         "protein %3d, sodium %4d, fiber %4d\n") % \
                (v.varValue, name, kcal_times_servings, carb_times_servings,
                 fat_times_servings, protein_times_servings,
                 sodium_times_servings, fiber_times_servings)

            if menu_str in dict_of_menus.keys():
                menu_found_flag = 1
            else:
                dict_of_menus[menu_str] = ''

    if menu_found_flag == 1:
        continue

    menu_num += 1

    print(f"Menu #{menu_num}")

    # Print the variables optimized value
    print(110 * '-')
    total_kcal = 0
    total_carb = 0
    total_fat = 0
    total_protein = 0
    total_sodium = 0
    total_fiber = 0
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
        fiber = food['fiber_per_serving']
        fiber_times_servings = fiber * v.varValue
        protein = food['protein_per_serving']
        protein_times_servings = protein * v.varValue
        sodium = food['sodium_per_serving']
        sodium_times_servings = sodium * v.varValue
        price = food['price_per_serving']
        price_times_servings = price * v.varValue
        total_kcal += kcal_times_servings
        total_carb += carb_times_servings
        total_fat += fat_times_servings
        total_fiber += fiber_times_servings
        total_protein += protein_times_servings
        total_sodium += sodium_times_servings
        total_price += price_times_servings
        if v.varValue > 0:
            print(("%dx %-30s kcal %4d, carb %4d, fat %3d, protein %3d, " +
                   "sodium %4d, fiber %4d, $%6.2f") %
                  (v.varValue, name, kcal_times_servings, carb_times_servings,
                   fat_times_servings, protein_times_servings,
                   sodium_times_servings, fiber_times_servings,
                   price_times_servings))

    carb_percent = (total_carb * 4 / total_kcal) * 100
    fat_percent = (total_fat * 9 / total_kcal) * 100
    protein_percent = (total_protein * 4 / total_kcal) * 100
    protein_factor = total_protein / BMI.lbs_to_kg(current_weight_lbs)

    print(110 * '-')
    print(("%-33s kcal %4d, carb %4d, fat %3d, protein %3d, "
           "sodium %4d, fiber %4d, $%6.2f") %
          ("Totals:", total_kcal, total_carb, total_fat,
           total_protein, total_sodium, total_fiber, total_price))

    print("%-33s %4.1f%% carb / %4.1f%% fat / %4.1f%% protein (%3.1fg/kg)" %
          ("Nutrients:", carb_percent, fat_percent,
           protein_percent, protein_factor))
    print()
    for v in model.variables():
        name = v.name.replace('_', ' ')
        servings = int(v.varValue)
        if servings > 0:
            for i in range(1, servings + 1):
                print("[ ] %s" % (name))

    print()
    print(flush=True)

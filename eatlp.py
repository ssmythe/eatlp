#!/usr/bin/env python3

from src.foods import *
from src.food import *
from pulp import *

max_kcal = 1643
max_sodium = 2000

foods = Foods()
foods.read_foods_from_json_file('data/foods.json')
list_of_sorted_foods = sorted(foods.dict_of_foods.keys())

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
    expr += f"{food['sodium_per_serving']}*{key} +"
    i += 1
expr += "0 <= {max_sodium}"
globals()['model'] += eval(expr)

# Solve problem
model.solve(PULP_CBC_CMD(msg=False))

# Print the variables optimized value
total_kcal = 0
total_sodium = 0
for v in model.variables():
    name = v.name.replace('_', ' ')
    food = foods.dict_of_foods[name]
    kcal = food['kcal_per_serving']
    kcal_times_servings = kcal * v.varValue
    sodium = food['sodium_per_serving']
    sodium_times_servings = sodium * v.varValue
    total_kcal += kcal_times_servings
    total_sodium += sodium_times_servings
    if v.varValue > 0:
        print(f"{name}=x{v.varValue} kcal={kcal}/{kcal_times_servings} sodium={sodium}/{sodium_times_servings} ")
print("\nTotals: kcal =", total_kcal, "sodium =", total_sodium)

# The optimised objective function value is printed to the screen
print('Value of Objective Function =', value(model.objective))

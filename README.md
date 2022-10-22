# eatlp
meal planning to fit specific nutrition requirements using linear programming (PuLP)

# Initial setup

## Install requirements
```bash
pip install -r requirements.txt
```

## Create user details (user.json)
```bash
./create_user_json.py
```

## Generate weight loss schedule to determine target weight loss date
```bash
./weight_loss_schedule.py
```

# Daily use
## Adjust user.json to accomodate changes in weight and activity level
```bash
vi user.json
```

## Generate menus daily
```bash
./plan_menus.sh
```
Pick whichever menu seems good for the day.

---
# Adjust data files for your own use

## data/item.json

Used to represent items you buy at the store.

## data/recipe.json

Used to represent combinations of items.

Note: data/foods.json is generated by ./cook.py used by ./plan_menus.sh

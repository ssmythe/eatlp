# eatlp
meal planning to fit specific nutrition requirements using linear programming (PuLP)

# How to use

## Initial setup

### Install requirements
```bash
pip install -r requirements.txt
```

### Create user details (user.json)
```bash
./create_user_json.py
```

### Generate weight loss schedule to determine target weight loss date
```bash
./weight_loss_schedule.py
```

## Daily use
### Adjust user.json to accomodate changes in weight and activity level
```bash
vi user.json
```

### Generate menus daily
```bash
./plan_menus.sh
```
Pick whichever menu seems good for the day.

#!/usr/bin/env bash

./sort_items.py
./sort_recipes.py
./cook.py
./eatlp.py | tee menus.txt

#!/usr/bin/env bash

./cook.py
./display_recipes.py | tee recipes.txt

#!/usr/bin/env bash

./cook.py
./list_food_report.py $1 $2 | tee report.txt

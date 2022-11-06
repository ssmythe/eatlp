#!/usr/bin/env bash

./cook.py
./list_food_report.py -a | tee report.txt

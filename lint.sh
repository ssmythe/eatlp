#!/usr/bin/env bash

flake8 . --exit-zero --max-complexity=10 | tee lint.txt


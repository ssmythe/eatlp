#/usr/bin/env bash
# NOTE: can call with -vv to get more details

pytest --doctest-modules --cov --durations=10 $1

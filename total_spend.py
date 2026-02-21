#!/usr/bin/env python

import re

def calculate_total_from_file(filename):
    total_weekly_spend = 0.0
    menus_processed = 0

    try:
        # Use 'with' to safely open and automatically close the file
        with open(filename, "r") as file:
            for line in file:
                # Check if the line starts with 'Totals:'
                if "Totals:" in line:
                    # Regex finds the float value following the '$' symbol
                    match = re.search(r"\$\s*(\d+\.\d+)", line)
                    if match:
                        price = float(match.group(1))
                        total_weekly_spend += price
                        menus_processed += 1
        
        print(f"Menus identified: {menus_processed}")
        print(f"Total Weekly Spend: ${total_weekly_spend:.2f}")
        print("")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

if __name__ == "__main__":
    calculate_total_from_file("menus.txt")

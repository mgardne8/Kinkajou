"""This file will holds the final script for IPA2 assignment
    TODO: document IPA2 file
"""

import kinkajou as kj

# Load and sanatize data

## Import to DataCage using kinkajou
tuition_data = kj.cage_csv("../data/us_avg_tuition.csv", encoding="utf-8-sig")

## Correct DataCage headers due to poor data formatting
tuition_data.header = [x.strip() for x in tuition_data.header]

## Convert our tuition values from strings to integers for easy manipulation
for row in range(1, len(list(tuition_data.header))):
    tuition_data.modify_column(row, (lambda x: int(x.strip("$ ").replace(",", ""))))

# Main program loop/menu

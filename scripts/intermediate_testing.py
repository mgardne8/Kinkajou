"""
This file serves as a scrap scripts for intermediate testing
"""


import kinkajou as kj

# load the csv file to a DataCage
data = kj.cage_csv("../data/us_avg_tuition.csv", encoding="utf-8-sig")

# look at our header, and attempt to lead those excess spaces
print(f"\nHeader of file:\n{list(data.header)}")
print("Attempting to correct header data . . .")
data.header = [x.strip() for x in data.header]
print(f"Updated header of file:\n{list(data.header)}")

# Look at the head of our data and how poorly formatted the numerics are
print("\nHead(3) of file:")
data.head(3)

print("\nAttempting to Fix the poor formatting of values . . .")

# Define a callable function for this
def to_int(original) -> int:
    """throwaway callable to convert columns from string to int"""
    res = original.strip("$ ").replace(",", "")
    return int(res)


# iterate through all columns in table and update them with function
for x in range(1, len(list(data.header))):
    data.modify_column(x, to_int)

print("Updated Head(3) of file:")
data.head(3)

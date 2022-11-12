"""This file will holds the final script for IPA2 assignment
"""
import kinkajou as kj

#
# Load and sanatize data
#

tuition_data = kj.cage_csv("../data/us_avg_tuition.csv", encoding="utf-8-sig")

## Correct DataCage headers due to poor data formatting
tuition_data.header = [x.strip() for x in tuition_data.header]

## Convert our tuition values (columns 1 -> end) from strings to integers for easy manipulation
for row in range(1, len(list(tuition_data.header))):
    tuition_data.modify_column(row, (lambda x: int(x.strip("$ ").replace(",", ""))))


#
# Program specific functions
#


def statistics_state(state: str) -> None:
    """Attempt to fetch data for provided state and print it's statistics

    Args:
        state (str): state to search for in data
    """
    result = list(tuition_data.filter((lambda x: x[0].lower() == state.lower())))
    if result:
        print_statistics(result[0])
    else:
        print("╟──INVALID STATE")


def statistics_country() -> None:
    """Print statistics for average of all states in data"""

    country_data = []
    country_data.append("United States")

    # average all data columns and append them to a list matching the format of individual states
    for column in list(tuition_data.header)[1:]:
        values = list(tuition_data.column(column))
        country_data.append(sum(values) / len(values))

    print_statistics(country_data)


def print_statistics(data: list) -> None:
    """Print the Tutition statistics for the provided List

    Args:
        data (list): State or Country data in the format of ["Location", Year1data, ..., YearXdata]
    """

    # Create a list containing yearly tuition increases then calculate average increase
    increases = []
    for index, value in enumerate(data[2:]):
        increases.append(value - data[index + 1])
    inc_avg = sum(increases) / len(increases)

    print(f"╟──┬─ {data[0]}")
    print(f"║  ├─ Average tutition: ${sum(data[1:])/len(data[1:]) :.2f}")
    print(f"║  ├─ Average yearly tuition increase: ${inc_avg :.2f}")

    print("║  └─┬─Predicted tutions / based on...")
    print("║    ├─┬─ 1 year out:")
    print(f"║    │ ├─ Last tuition increase: ${data[-1] + increases[-1] :.2f}")
    print(f"║    │ └─ Avrg tuition increase: ${data[-1] + inc_avg :.2f}")

    print("║    └─┬─ 2 years out:")
    print(f"║      ├─ Last tuition increase: ${data[-1] + (increases[-1] * 2) :.2f}")
    # Sum of the last two increses is the same as twice the average of the last two... **math**
    print(f"║      ├─ Avrg last 2 increases: ${data[-1] + sum(increases[-2:]) :.2f}")
    print(f"║      └─ Avrg tuition increase: ${data[-1] + (inc_avg * 2 ) :.2f}")


#
# Main loop
#

DONE = False
print("╔════ Welcome to the US Tution Statistics Data Query Tool")

while not DONE:
    print("║")
    print("╟──┬─Please Make a selection:")
    print("║  ├─ 1: Full US Data")
    print("║  ├─ 2: Query Specific State")
    print("║  ├─ 3: Exit the program")
    choice = input("║  └───> ")
    print("║")

    match choice:
        case "1":
            statistics_country()
        case "2":
            print("╟──┬─Please enter state name:")
            choice_state = input("║  └───> ")
            print("║")
            statistics_state(choice_state)
        case "3":
            DONE = True
        case _:
            print("╟──INVALID INPUT")

print("╚════ Good Bye!")

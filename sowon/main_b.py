import json

# Create the dictionary representation of the employee schedule
employee_schedule = {
    "employee": {
        "Name": None,
        "ID": None,
        "Shift": None,
        "Monday": {
            "In": None,
            "Out": None,
            "Lunch": None,
            "Hr": None
        },
        "Tuesday": {
            "In": None,
            "Out": None,
            "Lunch": None,
            "Hr": None
        },
        "Wednesday": {
            "In": None,
            "Out": None,
            "Lunch": None,
            "Hr": None
        },
        "Thursday": {
            "In": None,
            "Out": None,
            "Lunch": None,
            "Hr": None
        },
        "Friday": {
            "In": None,
            "Out": None,
            "Lunch": None,
            "Hr": None
        },
        "Saturday": {
            "In": None,
            "Out": None,
            "Lunch": None,
            "Hr": None
        },
        "Sunday": {
            "In": None,
            "Out": None,
            "Lunch": None,
            "Hr": None
        }
    }
}

# Write the JSON object to a file
with open('data/employee_schedule.json', 'w') as file:
    json.dump(employee_schedule, file, indent=4)

# Read the JSON object back from the file to verify
with open('data/employee_schedule.json', 'r') as file:
    loaded_schedule = json.load(file)

print(loaded_schedule)

import json, random

# Add the directory containing main.py and other modules to sys.path
import sys, os
script_dir = os.path.dirname(os.path.realpath(__file__))
if script_dir not in sys.path:
    sys.path.append(script_dir)


from singleton import FileManager










file_manager = FileManager()

# Sample JSON structure as provided
employee_json = '''
{
    "Name": null,
    "ID": null,
    "Shift": null,
    "Monday": {"In": null, "Out": null, "Lunch": null, "Hr": null},
    "Tuesday": {"In": null, "Out": null, "Lunch": null, "Hr": null},
    "Wednesday": {"In": null, "Out": null, "Lunch": null, "Hr": null},
    "Thursday": {"In": null, "Out": null, "Lunch": null, "Hr": null},
    "Friday": {"In": null, "Out": null, "Lunch": null, "Hr": null},
    "Saturday": {"In": null, "Out": null, "Lunch": null, "Hr": null},
    "Sunday": {"In": null, "Out": null, "Lunch": null, "Hr": null}
}
'''


# Function to convert employee data to TSV format
def convert_to_tsv(employees):
    tsv_data = "Name\tID\tShift\tMon In\tMon Out\tMon Lunch\tMon Hr\tTue In\tTue Out\tTue Lunch\tTue Hr\tWed In\tWed Out\tWed Lunch\tWed Hr\tThu In\tThu Out\tThu Lunch\tThu Hr\tFri In\tFri Out\tFri Lunch\tFri Hr\tSat In\tSat Out\tSat Lunch\tSat Hr\tSun In\tSun Out\tSun Lunch\tSun Hr\n"
    for emp in employees:
        tsv_data += f"{emp['Name']}\t{emp['ID']}\t{emp['Shift']}\t"
        tsv_data += f"{emp['Monday']['In']}\t{emp['Monday']['Out']}\t{emp['Monday']['Lunch']}\t{emp['Monday']['Hr']}\t"
        tsv_data += f"{emp['Tuesday']['In']}\t{emp['Tuesday']['Out']}\t{emp['Tuesday']['Lunch']}\t{emp['Tuesday']['Hr']}\t"
        tsv_data += f"{emp['Wednesday']['In']}\t{emp['Wednesday']['Out']}\t{emp['Wednesday']['Lunch']}\t{emp['Wednesday']['Hr']}\t"
        tsv_data += f"{emp['Thursday']['In']}\t{emp['Thursday']['Out']}\t{emp['Thursday']['Lunch']}\t{emp['Thursday']['Hr']}\t"
        tsv_data += f"{emp['Friday']['In']}\t{emp['Friday']['Out']}\t{emp['Friday']['Lunch']}\t{emp['Friday']['Hr']}\t"
        tsv_data += f"{emp['Saturday']['In']}\t{emp['Saturday']['Out']}\t{emp['Saturday']['Lunch']}\t{emp['Saturday']['Hr']}\t"
        tsv_data += f"{emp['Sunday']['In']}\t{emp['Sunday']['Out']}\t{emp['Sunday']['Lunch']}\t{emp['Sunday']['Hr']}\n"
    return tsv_data



# Create two employee dictionaries from the template
employees = []
for i in range(2):  # Create two employees
    # Load the JSON data
    employee = json.loads(employee_json)  # Reload the template for each new employee
    employee['Name'] = f"Employee {i+1}"
    employee['ID'] = f"E10{i+1}"
    employee['Shift'] = f"Shift {i+1}"
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    in_time = 8 + i  # Different start times for demonstration
    out_time = 17 + i
    lunch_duration = 60
    hours_worked = (out_time - in_time) - lunch_duration / 60
    for day in days:
        employee[day]['In'] = in_time
        employee[day]['Out'] = out_time
        employee[day]['Lunch'] = lunch_duration
        employee[day]['Hr'] = hours_worked
    employees.append(employee)

# Convert to TSV
tsv_output = convert_to_tsv(employees)
file_manager.write(tsv_output, "data/out.tsv")
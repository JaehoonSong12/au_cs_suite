
import json





# Add the directory containing main.py and other modules to sys.path
import sys, os
script_dir = os.path.dirname(os.path.realpath(__file__))
if script_dir not in sys.path:
    sys.path.append(script_dir)


from singleton import TabularManager, DateManager









# Singleton instances
tabular_manager = TabularManager()
date_manager = DateManager()

# Reading a CSV file -> JSON
json_data = tabular_manager.read_csv("data/punch_report-raw_data.csv")
print(json_data)


# Printing each JSON object in human-readable format
print("CSV Data in Human-Readable Format:")
for index, item in enumerate(json_data, start=1):
    print(f"Row {index}:")
    print(json.dumps(item, indent=2))
    print()  # Add a blank line for better separation























###############################################3
###############################################3 Specific Personal Customization
###############################################3

def normalize_json_data(data):
    """
    Normalizes the JSON data by combining first and last names into a single name field
    and filtering out unnecessary fields.

    Args:
    data (List[Dict[str, Union[str, int, float]]]): The list of dictionaries representing the JSON data.

    Returns:
    List[Dict[str, str]]: A list of dictionaries with normalized data.
    """
    normalized_data = []
    for entry in data:
        normalized_entry = {
            "Name": f"{entry['EMP F NAME']} {entry['EMP L NAME']}",
            "Date": date_manager.get_day_of_week(entry["DATE"]),
            "In": entry["IN"],
            "Out": entry["OUT"]
        }
        normalized_data.append(normalized_entry)

    return normalized_data







# Example of using the function with your JSON data
normalized_json = normalize_json_data(json_data)
print("Normalized JSON Data:")
for index, item in enumerate(normalized_json, start=1):
    print(f"Row {index}:")
    print(json.dumps(item, indent=2))
    print()  # Add a blank line for better separation



# # Writing to a CSV file
# tabular_manager.write_tabular(json_data, "output.csv", "csv")




# # Reading a TSV file
# tsv_data = tabular_manager.read_tsv("data.tsv")
# print(tsv_data)


# # Writing to a TSV file
# tabular_manager.write_tabular(tsv_data, "output.tsv", "tsv")

def run():
    print()

# Example usage:
if __name__ == "__main__":
    run()
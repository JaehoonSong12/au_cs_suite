import csv

with open('your_file.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)


# -------------------------------------

union_set = set1.union(set2)

my_set = {1, 2, 3, 4, 5}

for element in my_set:
    # Process the element here
    print(element * 2)


my_string = " Hello World! "

my_string_to_compare = my_string.replace(" ", "").lower()



def names_match(name1, name2):
    # Split both names into parts by whitespace
    name1_parts = name1.strip().split()
    name2_parts = name2.strip().split()
    
    # Extract the first and last names
    first_name1, last_name1 = name1_parts[0], name1_parts[-1]
    first_name2, last_name2 = name2_parts[0], name2_parts[-1]
    
    # Compare first and last names (case-insensitive)
    return first_name1.lower() == first_name2.lower() and last_name1.lower() == last_name2.lower()

# Example usage:
name1 = "John   Michael Smith"
name2 = "John Smith"
print(names_match(name1, name2))  # Output: True

system1_name = "John A. Smith"
system2_name = "john smith"

# Verify if both systems refer to the same user
if names_match(system1_name, system2_name):
    print("The names match!")  # Output: The names match!
else:
    print("The names don't match!")

#Dictionary
ep1 = {
    'EmployeeID': 221092,
    'EmployeeName': 'Fredrick Zocco',
    'Number of Experience': 2,
    'Current Position': 'Research Scientist'
}

# New details to update the dictionary
updates = {
    'EmployeeID': 69420,
    'EmployeeName': 'Jamie',
    'Number of Experience': 1,
    'Current Position': 'Top G'
}

# Using a FOR loop to update the dictionary
for key in ep1.keys():
    if key in updates:
        ep1[key] = updates[key]

print(ep1)

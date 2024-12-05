#Dictionary
ep1 = {
    'EmployeeID': 221092,
    'EmployeeName': 'Fredrick Zocco',
    'Number of Experience': 2,
    'Current Position': 'Research Scientist'}
print(f'Before changes {ep1}')

for emp_data in ep1:
    if emp_data == 'EmployeeID':
        ep1[emp_data] = '5010'
    elif emp_data == 'EmployeeName':
        ep1[emp_data] = 'Jamie'
    elif emp_data == 'Number of Experience':
        ep1[emp_data] = 1
    else:
        ep1[emp_data] = 'Top G'

print(f'After changes {ep1}')
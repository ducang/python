salary = [
    {
    'Name' : 'Huy',
    'Role' : 'Waiter',
    'Hours' : 12,
    'Salary per Hour($)': 0.8 
    },
    {
    'Name' : 'Tung',
    'Role' : 'Cook',
    'Hours' : 24,
    'Salary per Hour($)': 1.5 
    },
    {
    'Name' : 'M.Duc',
    'Role' : 'Manager',
    'Hours' : 20,
    'Salary per Hour($)': 2
    },
    {
    'Name' : 'Don',
    'Role' : 'Waiter',
    'Hours' : 12,
    'Salary per Hour($)': 0.9
    },
    {
    'Name' : 'H.Duc',
    'Role' : 'Waiter',
    'Hours' : 14,
    'Salary per Hour($)': 0.7
    } 
]

# print(salary[2])

salary[0] = {
    'Huyen' : 'Waitress',
    'Hours' : 14,
    'Salary per Hour($)' : 1
}

# print(salary)

# salary.pop(4)
# print(salary)

# for salaries in salary:
#     print(salaries)

length = len(salary)

for i in range(length):
    a = salary[i]
    b = a['Hours']
    c = a['Salary per Hour($)']
    d = b * c * 30
    print(d)

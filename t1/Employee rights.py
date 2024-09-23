employees = {
    'John': {'department': 'Engineering', 'salary': 70000},
    'Jane': {'department': 'HR', 'salary': 65000},
    'Alice': {'department': 'Marketing', 'salary': 60000},
    'Bob': {'department': 'Sales', 'salary': 55000},
    'Charlie': {'department': 'Engineering', 'salary': 72000},
    'Diana': {'department': 'HR', 'salary': 68000},
    'Eve': {'department': 'Finance', 'salary': 75000},
    'Frank': {'department': 'IT', 'salary': 70000},
    'Grace': {'department': 'Marketing', 'salary': 62000},
    'Hank': {'department': 'Sales', 'salary': 57000}
}
analysis_list = {}
sections = []
while True:
    item = input('Enter the sections you want to review  ')
    if item == '':
        break
    sections.append(item)


def filter_by_department(employees, department):
    salary_list = []
    for item in employees.values():
        if item['department'] == department:
            salary_list.append(item['salary'])
    return salary_list


for a in sections:
    department = filter_by_department(employees, a)
    avg_salary = sum(department) / len(department)
    analysis_list.update({a: avg_salary})

for b in analysis_list:
    print(f'department {b} average salary : {analysis_list[b]}')

min_average = min(analysis_list,key=analysis_list.get)
max_average = max(analysis_list,key=analysis_list.get)

print(f'department with highest average salary : {max_average} ({analysis_list[max_average]})\n'
      f'department with Lowest average salary : {min_average}({analysis_list[min_average]})')
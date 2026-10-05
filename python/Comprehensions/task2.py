numbers = [1, 2, 3, 4, 5]

square_dic = {num : num * num for num in numbers}
print(square_dic)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_and_square_dic = {num : num * num for num in numbers if num % 2 == 0}
print(even_and_square_dic)

employees = {
    "Om": 50000,
    "Rahul": 45000,
    "Amit": 60000,
    "Raj": 35000
}

salary_greater_45000 = {name : salary for name,salary in employees.items() if salary > 45000}
print(salary_greater_45000) 

# You can use filter() also

# high_salary = filter(
#     lambda employee: employee["salary"] > 50000,
#     employees
# )

# print(list(high_salary))
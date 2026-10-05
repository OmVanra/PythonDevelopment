def calculate_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

sum = calculate_sum(10, 20, 30)
print("sum is ", sum)

def employee_info(**kwargs):
    print("name :", kwargs["name"])
    print("age :", kwargs["age"])
    print("department :", kwargs["department"])
    print("salary :", kwargs["salary"])

employee_info(
    name="Om",
    age=20,
    department="IT",
    salary=50000
)

def calculate_average(*args):
    average = 0
    total = 0
    total_num = 0
    for num in args:
        total += num
        total_num += 1
    average = total / total_num
    return average

print(calculate_average(10, 20, 30, 40, 50))
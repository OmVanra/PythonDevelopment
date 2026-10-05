# def process_numbers(numbers):
#     ...

# Given:

# numbers = [10, 15, 20, 25, 30, 35, 40]

# Your function should:

# Remove numbers below 20
# Square the remaining numbers
# Return the result as a list

def process_numbers(numbers):
    filtered_numbers = [num for num in numbers if num >= 20]
    squared_numbers = [num ** 2 for num in filtered_numbers]
    return squared_numbers

# Test
numbers = [10, 15, 20, 25, 30, 35, 40]
result = process_numbers(numbers)
print(result)
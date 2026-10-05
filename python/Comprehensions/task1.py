numbers = [2, 4, 6, 8, 10]

square_num = [num * num for num in numbers]
print(square_num)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_greater_than_5 = [num for num in numbers if num > 5]
print(num_greater_than_5) 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square_even_only = [num * num for num in numbers if num % 2 == 0]
print(square_even_only)
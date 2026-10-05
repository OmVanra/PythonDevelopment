numbers = [1, 2, 2, 3, 3, 4, 4, 5]

squares = {num*num for num in numbers}
print(squares)

numbers = [10, 15, 20, 25, 30, 35, 40]
ans2 = {num for num in numbers if num % 5 == 0 and num > 20}
print(ans2)

words = ["python", "java", "python", "sql", "java", "fastapi"]
length = {len(word) for word in words }

print(length)
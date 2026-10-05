# 🎯 Practice 3 — Decorator

# Create:

# @logger
# def add(a, b):
#     return a + b

# The decorator should print:

# Calling add
# Result: 30

# for:
# add(10, 20)
# Use @wraps.

def logger(func):
    from functools import wraps

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrapper

@logger
def add(a, b):
    return a + b

add(10, 20)


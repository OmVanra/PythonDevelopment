import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.2f} seconds")
        return result
    return wrapper


@timer
def calculate():
    total = 0

    for i in range(1_000_000):
        total += i

    return total


print(calculate())


from functools import wraps

session = {"logged_in": False}


def login():
    session["logged_in"] = True
    print("Logged in successfully")


def logout():
    session["logged_in"] = False
    print("Logged out")


def authentication_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session["logged_in"]:
            print("Access denied. Please log in first.")
            return None
        return func(*args, **kwargs)
    return wrapper


@authentication_required
def dashboard():
    print("Welcome to dashboard")


# Test
dashboard()      # not logged in

login()
dashboard()      # logged in

logout()
dashboard()      # logged out again
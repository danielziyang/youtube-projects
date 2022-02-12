def my_decorator(some_function):
    def wrapper(*args, **kwargs):
        print("do something before")
        some_function(*args, **kwargs)
        print("do something after")
    
    return wrapper 

@my_decorator
def addition(a, b):
    print(a+b)


addition(4,5)
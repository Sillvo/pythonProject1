# Factorial generator
def factorial():
    index = 0
    product = 1
    while True:
        yield product
        index += 1
        product *= index

# Power closure
def power(x):
    def inner(n):
        return x ** n
    return inner

# Exponential function
def exp(x, n):
    fact = factorial()
    pow_x = power(x)
    return sum(pow_x(i) / next(fact) for i in range(n))

print(exp(1, 10))  # e^1 with 10 terms

def logger(func):
    def wrapper(*args, **kwargs):
        #print(f"Calling function {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("world")  # Logs: Calling function greet with arguments ('world',) and keyword arguments {}
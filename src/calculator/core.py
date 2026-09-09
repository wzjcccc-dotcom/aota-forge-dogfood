def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    result = a / b
    # Return int if result is integral and inputs were ints
    if isinstance(a, int) and isinstance(b, int) and result.is_integer():
        return int(result)
    return result

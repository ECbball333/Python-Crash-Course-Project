

def add(a, b): return a + b
def safe_div(a, b):
    if b == 0:
        raise ZeroDivisionError('b cannot = zero')
    return a / b
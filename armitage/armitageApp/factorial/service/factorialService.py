import math
from functools import lru_cache

def sanitizeAndCalculate(n):
    if not isinstance(n, int):
        return None
    elif n < 0:
        return None
    else:
        return calculate(n)
        
def calculate(n):
    return math.factorial(n)
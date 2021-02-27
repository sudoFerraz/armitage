from functools import lru_cache

def sanitizeAndCalculate(m, n):
    if not isinstance(m, int) or not isinstance(n, int):
        return None
    else:
        return ackermann(m, n)

@lru_cache()
def ackermann(m, n):
  if m == 0:
    return n+1
  else:
    if n == 0:
      return ackermann(m-1, 1)
    else:
      return ackermann(m-1, ackermann(m, n-1))
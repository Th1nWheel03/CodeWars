import math

def multiply(n):
    if n < 0:
        puissance = math.ceil(math.log10(-n))
    else:
        puissance = math.ceil(math.log10(n + 1))
    return round(n * math.pow(5, puissance), None)

print(multiply(3))
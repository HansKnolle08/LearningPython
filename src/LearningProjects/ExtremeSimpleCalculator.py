def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Kann nicht durch null teilen"
    else:
        return a / b

print(add(1, 4))
print(sub(1, 5))
print(mul(4, 2))
print(div(8, 2))
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
    
running = True

while running:
    operation = input("Gib eine Operation ein:\n")
    if operation == "+":
        x = float(input("Gib die erste Zahl ein:\n"))
        y = float(input("Gib die zweite Zahl ein:\n"))
        print(add(x, y))
    elif operation == "-":
        x = float(input("Gib die erste Zahl ein:\n"))
        y = float(input("Gib die zweite Zahl ein:\n"))
        print(sub(x, y))
    elif operation == "*":
        x = float(input("Gib die erste Zahl ein:\n"))
        y = float(input("Gib die zweite Zahl ein:\n"))
        print(mul(x, y))
    elif operation == "/":
        x = float(input("Gib die erste Zahl ein:\n"))
        y = float(input("Gib die zweite Zahl ein:\n"))
        print(div(x, y))
    else:
        quit()
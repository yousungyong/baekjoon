def is_divisor(a, b):
    return b % a == 0

def is_multiple(a, b):
    return a % b == 0

def process_input(a, b):
    if is_divisor(a, b):
        print("factor")
    elif is_multiple(a, b):
        print("multiple")
    else:
        print("neither")

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    process_input(a, b)
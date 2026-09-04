a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def check(a, b):
    if a + b < 100:
        return a + b
    else:
        return a - b
print("Output: ", check(a, b))

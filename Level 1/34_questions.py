a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def check(a, b):
    at = (a // 10) % 10
    bt = (b // 10) % 10
    if at > bt:
        return abs((a % 10) - (a // 100))
    else:
        return abs((b % 10) - (b // 100))
print("Output: ", check(a, b))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def check(a, b):
    x = (a // 100) + (a % 10)
    y = (b // 100) + (b % 10)
    if x > y:
        return (a // 100) + ((a // 10) % 10) + (a % 10)
    else:
        return (b // 100) + ((b // 10) % 10) + (b % 10)
print("Output: ", check(a, b))

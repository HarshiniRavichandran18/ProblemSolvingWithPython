a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def check(a, b):
    if a > b:
        return (a // 10) + (a % 10)
    else:
        return (b // 10) + (b % 10)
print("Output: ", check(a, b))

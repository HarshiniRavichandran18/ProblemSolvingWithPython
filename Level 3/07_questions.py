def check(a, b):
    if a == b:
        return "Same"
    else:
        return "Not Same"
a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))
print("Output: ", check(a, b))

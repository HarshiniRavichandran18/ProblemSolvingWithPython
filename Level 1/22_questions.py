a = int(input("Enter a Number: "))
def odd(a):
    return a - ((a // 10) % 2) * 5
print("Output: ", odd(a))

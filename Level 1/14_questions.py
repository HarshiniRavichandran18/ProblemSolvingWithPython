a = int(input("Enter a Number: "))
def rev(a):
    return ((a % 10) * 100) + ((a // 10) % 10) * 10 + (a // 100)
print("Output: ", rev(a))

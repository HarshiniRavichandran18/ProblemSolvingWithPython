a = int(input("Enter a Number: "))
def rev(a):
    return (a // 100) % 10 * 1000 + (a // 1000) * 100 + (a % 100)
print("Output: ", rev(a))

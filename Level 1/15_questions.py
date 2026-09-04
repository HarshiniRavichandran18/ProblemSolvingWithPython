a = int(input("Enter a Number: "))
def rev(a):
    return (a // 100) * 100 + (a % 10) * 10 + ((a // 10) % 10)
print("Output: ", rev(a))

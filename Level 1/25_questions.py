a = int(input("Enter a Number: "))
def same(a):
    return a - ((((a // 10) % 10) == ((a // 100) % 10)) * 5)
print("Output: ", same(a))

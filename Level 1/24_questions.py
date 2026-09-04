a = int(input("Enter a Number: "))
def same(a):
    return a - ((a // 100 == a % 10) * 5)
print("Output: ", same(a))

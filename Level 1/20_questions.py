a = int(input("Enter a Number: "))
def ones(a):
    return (a // 100) * 100 + (a % 10)
print("Output: ", ones(a))

def check(a):
    return (a % 10) * 100 + ((a // 10) % 10) * 10 + (a // 100)
a = int(input("Enter a Number: "))
print("Output: ", check(a))

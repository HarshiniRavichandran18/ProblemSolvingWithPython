def check(a):
    return (a % 10) * 1000 + ((a // 10) % 10) * 100 + ((a // 100) % 10) * 10 + (a // 1000)
a = int(input("Enter a Number: "))
print("Output: ", check(a))

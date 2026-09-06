def check(a):
    return (a // 1000) + ((a // 100) % 10) + ((a // 10) % 10) + (a % 10)
a = int(input("Enter a Number: "))
print("Output: ", check(a))

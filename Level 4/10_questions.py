def check(a):
    return (a // 100) + ((a // 10) % 10) + (a % 10)
a = int(input("Enter a Number: "))
print("Output: ", check(a))

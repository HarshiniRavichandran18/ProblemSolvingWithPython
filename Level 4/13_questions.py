def check(a):
    sum = 0
    while a > 0:
        sum = sum + (a % 10)
        a = a // 10
    return sum
a = int(input("Enter a Number: "))
print("Output: ", check(a))

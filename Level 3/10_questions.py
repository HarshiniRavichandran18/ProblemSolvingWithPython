def check(a):
    count = 0
    while a > 0:
        a = a // 10
        count = count + 1
    return count
a = int(input("Enter a Number: "))
print("Output: ", check(a))

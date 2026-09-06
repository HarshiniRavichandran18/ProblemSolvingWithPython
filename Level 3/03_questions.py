def check(a):
    sum = 0
    while a > 0:
        sum = sum + (a % 10)
        a = a // 10
    if sum == 14:
        return "Sum of Digits is 14"
    else:
        return "Sum of Digits is not 14"
a = int(input("Enter a Number: "))
print("Output: ", check(a))

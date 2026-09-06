def check(a):
    while a >= 10:
        digit1 = a % 10
        a = a // 10
        digit2 = a % 10
        if digit2 >= digit1:
            return "No"
    return "Yes"
a = int(input("Enter a Number: "))
print("Output: ", check(a))

a = int(input("Enter a Number: "))
def sum_digit(a):
    s = (a // 100) + ((a // 10) % 10) + (a % 10)
    while s >= 10:
        s = (s // 10) + (s % 10)
    return s
print("Output: ", sum_digit(a))

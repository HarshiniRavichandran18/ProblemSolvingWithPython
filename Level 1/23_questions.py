a = int(input("Enter a Number: "))

def sum_odd(a):
    return a - (((a // 10) + (a % 10)) % 2) * 5

print("Output: ", sum_odd(a))

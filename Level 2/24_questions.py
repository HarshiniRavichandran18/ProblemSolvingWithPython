a = int(input("Enter a Number: "))
count = 0
while a >= 10:
    digit = a % 100
    if digit == 16 or digit == 25 or digit == 36 or digit == 49 or digit == 64 or digit == 81:
        count = count + 1
    a = a // 10
print("Output: ", count)

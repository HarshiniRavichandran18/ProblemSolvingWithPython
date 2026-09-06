a = int(input("Enter a Number: "))
count = 0
while a > 0:
    digit = a % 10
    if digit == 1 or digit == 4 or digit == 9:
        count = count + 1
    a = a // 10
print("Output: ", count)

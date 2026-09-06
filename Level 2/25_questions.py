a = int(input("Enter a Number: "))
count = 0
while a > 0:
    digit = a % 10
    if digit == 2 or digit == 3 or digit == 5 or digit == 7:
        count = count + 1
    a = a // 10
print("Output: ", count)

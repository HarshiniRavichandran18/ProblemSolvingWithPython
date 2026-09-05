a = int(input("Enter a Number: "))
count = 0
while a > 0:
    digit = a % 10
    if digit % 2 != 0:
        count = count + 1
    a = a // 10
print("Output: ", count)

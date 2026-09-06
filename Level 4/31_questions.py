count = 0
for i in range(1, 1001):
    a = i
    while a > 0:
        digit = a % 10
        if digit == 0:
            count = count + 1
        a = a // 10
print("Output: ", count)

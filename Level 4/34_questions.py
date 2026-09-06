count = 0
for i in range(1, 100000):
    a = i
    rev = 0
    while a > 0:
        rev = rev * 10 + (a % 10)
        a = a // 10
    if i == rev:
        count = count + 1
print("Output: ", count)

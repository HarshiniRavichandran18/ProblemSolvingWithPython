count = 0
for i in range(2, 1000000):
    factors = 0
    for j in range(1, i + 1):
        if i % j == 0:
            factors = factors + 1
    if factors == 2:
        a = i
        sum = 0
        while a > 0:
            sum = sum + (a % 10)
            a = a // 10
        if sum == 14:
            count = count + 1
print("Output: ", count)

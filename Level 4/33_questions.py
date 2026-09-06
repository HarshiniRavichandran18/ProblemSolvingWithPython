count = 0
for i in range(1000, 10000):
    a = i
    d1 = a // 1000
    d2 = (a // 100) % 10
    d3 = (a // 10) % 10
    d4 = a % 10
    if d1 <= d2 and d2 <= d3 and d3 <= d4:
        count = count + 1
print("Output: ", count)

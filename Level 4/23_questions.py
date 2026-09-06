sum = 0
for i in range(1, 10):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count = count + 1
    if count == 2:
        sum = sum + i
print("Output: ", sum)

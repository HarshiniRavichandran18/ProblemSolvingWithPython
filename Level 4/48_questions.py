a = [6, 12, 3, 15, 7]
for i in range(len(a) - 1, 0, -1):
    if a[i] >= 10:
        carry = a[i] // 10
        a[i] = a[i] % 10
        a[i - 1] = a[i - 1] + carry
print("Output: ", *a)

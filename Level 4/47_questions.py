a = list(map(int, input("Enter first Array: ").split()))
b = list(map(int, input("Enter second Array: ").split()))
result = []
carry = 0
i = len(a) - 1
j = len(b) - 1
while i >= 0 or j >= 0 or carry:
    x = a[i] if i >= 0 else 0
    y = b[j] if j >= 0 else 0
    total = x + y + carry
    result.append(total % 10)
    carry = total // 10
    i = i - 1
    j = j - 1
result.reverse()
print("Output: ", result)

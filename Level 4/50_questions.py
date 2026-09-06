def add(a, b):
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = ""
    while i >= 0 or j >= 0 or carry:
        x = int(a[i]) if i >= 0 else 0
        y = int(b[j]) if j >= 0 else 0
        total = x + y + carry
        result = str(total % 10) + result
        carry = total // 10
        i = i - 1
        j = j - 1
    return result
a = input("Enter first Number: ")
b = input("Enter second Number: ")
print("Output: ", add(a, b))

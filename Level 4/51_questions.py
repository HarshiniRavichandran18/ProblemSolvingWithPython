a = input("Enter String: ")
b = input("Enter Character: ")
result = []
for i in range(len(a)):
    if a[i] == b:
        result.append(i + 1)
print("Output: ", *result, sep=", ")

def check(a):
    result = ""
    for i in a:
        result = result + chr(i + 48)
    return result
a = list(map(int, input("Enter Array: ").split()))
print("Output: ", check(a))

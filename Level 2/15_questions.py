a = int(input("Enter a Number: "))
def check(a):
    first = a
    while first >= 10:
        first = first // 10
    if first % 2 == 0:
        return a
    else:
        return a - (10 ** (len(str(a)) - 1))
print("Output: ", check(a))

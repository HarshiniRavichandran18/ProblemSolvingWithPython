a = int(input("Enter a Number: "))
def check(a):
    if (a % 10) + (a // 100) < 10:
        return "Success"
    else:
        return "Failure"
print("Output: ", check(a))

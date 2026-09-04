a = int(input("Enter a Number: "))
def check(a):
    if (a // 100) + ((a // 10) % 10) + (a % 10) == 10:
        return "Success"
    else:
        return "Failure"
print("Output: ", check(a))

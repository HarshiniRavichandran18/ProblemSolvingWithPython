a = int(input("Enter a Number: "))
def check(a):
    if (a // 10) % 10 + (a // 100) % 10 == 10 and ((a // 10) % 10 > 7 or (a // 100) % 10 > 7):
        return "Success"
    else:
        return "Failure"
print("Output: ", check(a))

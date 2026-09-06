def check(a):
    count = 0
    for i in range(1, a + 1):
        if a % i == 0:
            count = count + 1
    if count == 2:
        return "Number is Prime"
    else:
        return "Number is not Prime"
a = int(input("Enter a Number: "))
print("Output: ", check(a))

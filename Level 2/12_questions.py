a = int(input("Enter a Number: "))
sum = 0
while a>0:
    sum = sum + (a % 10)
    a = a // 10
print("Output: ", sum)

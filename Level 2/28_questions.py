a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))
if a > b:
    lcm = a
else:
    lcm = b
while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm = lcm + 1
print("Output: ", lcm)

a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))
c = int(input("Enter third Number: "))
if a > b and a > c:
    lcm = a
elif b > c:
    lcm = b
else:
    lcm = c
while True:
    if lcm % a == 0 and lcm % b == 0 and lcm % c == 0:
        break
    lcm = lcm + 1
print("Output: ", lcm)

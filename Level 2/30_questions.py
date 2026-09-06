a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))
if a > b:
    hcf = b
else:
    hcf = a
while hcf > 0:
    if a % hcf == 0 and b % hcf == 0:
        break
    hcf = hcf - 1
print("Output: ", hcf)

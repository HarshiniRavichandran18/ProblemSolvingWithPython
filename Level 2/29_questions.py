'''Question: Write a program to get three numbers from the user and print the LCM of 
those numbers. 
Testcase: 
Input: 2, 3, 4 → Output: 12 
Input: 4, 6, 8 → Output: 24 '''

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

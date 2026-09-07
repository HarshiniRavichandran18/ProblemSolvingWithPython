'''Question: Write a program to get two numbers from the user and print the LCM of those 
numbers. 
Testcase: 
Input: 12, 18 → Output: 36 
Input: 15, 20 → Output: 60'''

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

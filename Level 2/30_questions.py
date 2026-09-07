'''Question: Write a program to get two numbers from the user and print the HCF of those 
numbers. 
Testcase: 
Input: 12, 18 → Output: 6 
Input: 24, 36 → Output: 12'''

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

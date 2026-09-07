'''Question: Get two 2-digit numbers from user. If the sum of the numbers is less than 100, then 
print the sum, otherwise print the difference. 
Testcase: 
Input: 56, 78 → Output: 22 
Input: 14, 65 → Output: 79'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def check(a, b):
    if a + b < 100:
        return a + b
    else:
        return a - b
print("Output: ", check(a, b))

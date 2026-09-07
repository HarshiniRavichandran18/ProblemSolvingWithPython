'''Question: Get two 2-digit numbers from user. Print the sum of digits of the biggest number. 
Testcase: 
Input: 56, 78 → Output: 15 
Input: 14, 65 → Output: 11'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def check(a, b):
    if a > b:
        return (a // 10) + (a % 10)
    else:
        return (b // 10) + (b % 10)
print("Output: ", check(a, b))

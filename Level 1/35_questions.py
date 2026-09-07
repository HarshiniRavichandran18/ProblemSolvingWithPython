'''Question: Get two 3-digit numbers from user. Add the one's and hundred's digits of both 
numbers. Print the sum of all the digits of the number whose sum of one's and hundred's digits 
is bigger. 
Testcase: 
Input: 856, 978 → Output: 24 
Input: 128, 365 → Output: 11'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def check(a, b):
    x = (a // 100) + (a % 10)
    y = (b // 100) + (b % 10)
    if x > y:
        return (a // 100) + ((a // 10) % 10) + (a % 10)
    else:
        return (b // 100) + ((b // 10) % 10) + (b % 10)
print("Output: ", check(a, b))

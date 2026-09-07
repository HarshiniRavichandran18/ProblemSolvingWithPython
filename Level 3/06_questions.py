'''Question: Get a number from user and reverse that number. 
Testcase: 
Input: 123 → Output: 321 
Input: 56789 → Output: 98765'''

def check(a):
    rev = 0
    while a > 0:
        rev = rev * 10 + (a % 10)
        a = a // 10
    return rev
a = int(input("Enter a Number: "))
print("Output: ", check(a))

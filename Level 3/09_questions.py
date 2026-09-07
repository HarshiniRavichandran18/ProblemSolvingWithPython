'''Question: Get a two-digit number from user and swap the digits. 
Testcase: 
Input: 34 → Output: 43 
Input: 56 → Output: 65 '''

def check(a):
    return (a % 10) * 10 + (a // 10)
a = int(input("Enter a Number: "))
print("Output: ", check(a))

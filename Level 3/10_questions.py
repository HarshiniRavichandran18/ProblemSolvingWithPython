'''Question: Get a number from user, find the number of digits, and print it. 
Testcase: 
Input: 34678 → Output: 5 
Input: 12345678 → Output: 8'''

def check(a):
    count = 0
    while a > 0:
        a = a // 10
        count = count + 1
    return count
a = int(input("Enter a Number: "))
print("Output: ", check(a))

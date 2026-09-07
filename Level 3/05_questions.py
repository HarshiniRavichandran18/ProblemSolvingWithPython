'''Question: Get a number from user and count the number of zeros in that number. 
Testcase: 
Input: 100 → Output: 2 
Input: 1060030 → Output: 4'''

def check(a):
    count = 0
    while a > 0:
        digit = a % 10
        if digit == 0:
            count = count + 1
        a = a // 10
    return count
a = int(input("Enter a Number: "))
print("Output: ", check(a))

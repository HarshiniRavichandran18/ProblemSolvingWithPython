'''Question: Get a three-digit number from user. If the sum of the digits is less than 10, then print 
the sum, otherwise add the digits of the sum and continue until the result is a single digit. 
Testcase: 
Input: 123 → Output: 6 
Input: 149 → Output: 5 
Input: 991 → Output: 1'''

a = int(input("Enter a Number: "))
def sum_digit(a):
    s = (a // 100) + ((a // 10) % 10) + (a % 10)
    while s >= 10:
        s = (s // 10) + (s % 10)
    return s
print("Output: ", sum_digit(a))

'''Question: Get a two-digit number from user and subtract 5 from that number if the sum of the 
digits of the number is odd, then print the result. Do not use "if". 
Testcase: 
Input: 95 → Output: 95 
Input: 72 → Output: 67 '''

a = int(input("Enter a Number: "))

def sum_odd(a):
    return a - (((a // 10) + (a % 10)) % 2) * 5

print("Output: ", sum_odd(a))

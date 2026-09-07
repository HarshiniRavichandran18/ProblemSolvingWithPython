'''Question: Get a three-digit number from user and subtract 5 from that number if one's digit and 
hundred's digit are the same, then print the result. Do not use "if". 
Testcase: 
Input: 595 → Output: 590 
Input: 372 → Output: 372 '''

a = int(input("Enter a Number: "))
def same(a):
    return a - ((a // 100 == a % 10) * 5)
print("Output: ", same(a))

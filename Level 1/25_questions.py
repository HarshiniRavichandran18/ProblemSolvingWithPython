'''Question: Get a four-digit number from user and subtract 5 from that number if ten's digit 
position and hundred's digit position are the same, then print the result. Do not use "if". 
Testcase: 
Input: 7595 → Output: 7595 
Input: 3772 → Output: 3767'''

a = int(input("Enter a Number: "))
def same(a):
    return a - ((((a // 10) % 10) == ((a // 100) % 10)) * 5)
print("Output: ", same(a))

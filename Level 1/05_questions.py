'''Question: Get a number from user and divide by the number by 8 and print the remainder. 
Testcase: 
Input: 45 → Output: 5 
Input: 143 → Output: 7'''

def divd(n):
    return n%8
n = int(input("Enter a Integer: "))
print("Output: ", divd(n))

'''Question: Get a number from user and multiply 3 to that number and print the result. 
Testcase: 
Input: 45 → Output: 135 
Input: 1200 → Output: 3600'''

def mul(n):
    return n*3
n = int(input("Enter a Integer: "))
print("Output: ", mul(n))

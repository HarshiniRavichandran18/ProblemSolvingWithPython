'''Question: Get a number from user and subtract 5 to that number and print the result. 
Testcase: 
Input: 45 → Output: 40 
Input: 56789 → Output: 56784'''

def sub(n):
    return n-5
n = int(input("Enter a Integer: "))
print("Output: ", sub(n))

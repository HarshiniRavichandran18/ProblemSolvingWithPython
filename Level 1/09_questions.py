'''Question: Get a three-digit number from user and print the hundred's digit. 
Testcase: 
Input: 456 → Output: 4 
Input: 569 → Output: 5'''

a = int(input("Enter a Integer: "))
def tens(a):
    return a // 100
print("Output: ", tens(a))

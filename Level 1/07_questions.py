'''Question: Get a two-digit number from user and print the ten's digit. 
Testcase: 
Input: 45 → Output: 4 
Input: 56 → Output: 5'''

a = int(input("Enter a Integer: "))
def tens(a):
    return a // 10
print("Output: ", tens(a))

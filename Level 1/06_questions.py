'''Question: Get a two-digit number from user and print the one's digit. 
Testcase: 
Input: 45 → Output: 5 
Input: 56 → Output: 6'''

a = int(input("Enter a Integer: "))
def ones(a):
    return a % 10
print("Output: ", ones(a))

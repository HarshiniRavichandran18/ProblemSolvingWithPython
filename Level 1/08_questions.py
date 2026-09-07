'''Question: Get a three-digit number from user and print the one's digit. 
Testcase: 
Input: 456 → Output: 6 
Input: 569 → Output: 9'''

a = int(input("Enter a Integer: "))
def ones(a):
    return a % 10
print("Output: ", ones(a))

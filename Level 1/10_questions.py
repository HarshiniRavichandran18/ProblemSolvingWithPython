'''Question: Get a three-digit number from user and print the ten's digit. 
Testcase: 
Input: 456 → Output: 5 
Input: 569 → Output: 6'''

a = int(input("Enter a Integer: "))
def ones(a):
    return (a // 10) % 10
print("Output: ", ones(a))

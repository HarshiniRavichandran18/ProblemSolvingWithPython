'''Question: Get a two-digit number from user and print sum the digits. 
Testcase: 
Input: 56 → Output: 11 
Input: 69 → Output: 15 '''

a = int(input("Enter a Integer: "))
def ones(a):
    return (a // 10) + (a % 10)
print("Output: ", ones(a))

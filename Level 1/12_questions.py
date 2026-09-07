'''Question: Get a three-digit number from user and print sum the digits. 
Testcase: 
Input: 562 → Output: 13 
Input: 469 → Output: 19 '''

a = int(input("Enter a Integer: "))
def ones(a):
    return (a // 100) + ((a // 10) % 10) + (a % 10)
print("Output: ", ones(a))

'''Question: Get a three-digit number from user and make the ten's digit as 0, then print it. 
Testcase: 
Input: 695 → Output: 605 
Input: 182 → Output: 102'''

a = int(input("Enter a Number: "))
def ones(a):
    return (a // 100) * 100 + (a % 10)
print("Output: ", ones(a))

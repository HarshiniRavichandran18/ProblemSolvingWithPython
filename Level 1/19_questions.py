'''Question: Get a three-digit number from user and make the one's digit as 2, then print it. 
Testcase: 
Input: 695 → Output: 692 
Input: 182 → Output: 182'''

a = int(input("Enter a Number: "))
def ones(a):
    return (a // 10) * 10 + 2
print("Output: ", ones(a))

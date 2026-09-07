'''Question: Get a two-digit number from user and make the one's digit as 0, then print it. 
Testcase: 
Input: 95 → Output: 90 
Input: 18 → Output: 10 '''

a = int(input("Enter a Number: "))
def ones(a):
    return (a // 10)* 10
print("Output: ", ones(a))

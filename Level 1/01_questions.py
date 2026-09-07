'''Question: Get a number from user and add 2 to that number and print the result. 
Testcase: 
Input: 45 → Output: 47 
Input: 56789 → Output: 56791'''

def add(n):
    return n+2
n = int(input("Enter a Integer: "))
print("Output : ", add(n))

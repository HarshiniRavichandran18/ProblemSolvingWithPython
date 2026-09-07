'''Question: Get two numbers from user and compare them. If they are the same, print 
Same; otherwise print Not Same. 
Testcase: 
Input: 123, 123 → Output: Same 
Input: 56789, 12345 → Output: Not Same '''

def check(a, b):
    if a == b:
        return "Same"
    else:
        return "Not Same"
a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))
print("Output: ", check(a, b))

'''Question: Get a three-digit number from user and print the reverse of the number. 
Testcase: 
Input: 561 → Output: 165 
Input: 859 → Output: 958'''

a = int(input("Enter a Number: "))
def rev(a):
    return ((a % 10) * 100) + ((a // 10) % 10) * 10 + (a // 100)
print("Output: ", rev(a))

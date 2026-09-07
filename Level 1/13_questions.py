'''Question: Get a two-digit number from user and print the reverse of the number. 
Testcase: 
Input: 56 → Output: 65 
Input: 59 → Output: 95'''

a = int(input("Enter a Number: "))
def rev(a):
    return (a % 10) * 10 + (a // 10)
print("Output: ", rev(a))

'''Question: Get a four-digit number from user and only reverse the first two digits of the number, 
then print the number. 
Testcase: 
Input: 9561 → Output: 9516 
Input: 3859 → Output: 3895'''

a = int(input("Enter a Number: "))
def rev(a):
    return (a // 100) * 100 + (a % 10) * 10 + ((a // 10) % 10)
print("Output: ", rev(a))

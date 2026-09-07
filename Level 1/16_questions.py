'''Question: Get a four-digit number from user and only reverse the last two digits of the number, 
then print the number. 
Testcase: 
Input: 9561 → Output: 5961 
Input: 3859 → Output: 8359'''

a = int(input("Enter a Number: "))
def rev(a):
    return (a // 100) % 10 * 1000 + (a // 1000) * 100 + (a % 100)
print("Output: ", rev(a))

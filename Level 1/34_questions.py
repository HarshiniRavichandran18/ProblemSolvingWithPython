'''Question: Get two 3-digit numbers from user. Print the difference between the one's digit and 
hundred's digit of the number whose ten's digit is bigger than the other number's ten's digit. 
Testcase: 
Input: 856, 978 → Output: 1 
Input: 128, 365 → Output: 2'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def check(a, b):
    at = (a // 10) % 10
    bt = (b // 10) % 10
    if at > bt:
        return abs((a % 10) - (a // 100))
    else:
        return abs((b % 10) - (b // 100))
print("Output: ", check(a, b))

'''Question: Get a number from user and subtract 5 from that number if the number's ten's position 
digit is odd, then print the result. Do not use "if". 
Testcase: 
Input: 685 → Output: 685 
Input: 89172 → Output: 89167'''

a = int(input("Enter a Number: "))
def odd(a):
    return a - ((a // 10) % 2) * 5
print("Output: ", odd(a))

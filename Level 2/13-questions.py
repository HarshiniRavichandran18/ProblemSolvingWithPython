'''Question: Write a program to get a number from the user and print the reverse of that 
number. 
Testcase: 
Input: 123456 → Output: 654321 
Input: 76895439 → Output: 93459867 
Input: 675 → Output: 576 '''

a = int(input("Enter a Number: "))
rev = 0
while a > 0:
    rev = rev * 10 + (a % 10)
    a = a // 10
print("Output: ", rev)

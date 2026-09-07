'''Question: Write a program to get a number from the user and print the sum of all digits. 
 
Testcase: 
Input: 123456 → Output: 21 
Input: 76895439 → Output: 51 
Input: 675 → Output: 18'''

a = int(input("Enter a Number: "))
sum = 0
while a>0:
    sum = sum + (a % 10)
    a = a // 10
print("Output: ", sum)

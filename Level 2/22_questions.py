'''Question: Write a program to get a number from the user and print the total number of 
two-digit odd numbers in the number. 
Testcase: 
Input: 12345678 → Output: 3 
Input: 987531 → Output: 4'''

a = int(input("Enter a Number: "))
count = 0
while a > 0:
    digit = a % 100
    if digit >= 10 and digit % 2 != 0:
        count = count + 1
    a = a // 10
print("Output: ", count)

'''Question: Write a program to get a number from the user and print the total number of 
digits that are odd. 
Testcase: 
Input: 12345678 → Output: 4 
Input: 987531 → Output: 5'''

a = int(input("Enter a Number: "))
count = 0
while a > 0:
    digit = a % 10
    if digit % 2 != 0:
        count = count + 1
    a = a // 10
print("Output: ", count)

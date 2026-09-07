'''Question: Write a program to get a number from the user and print the total number of 
single-digit perfect square numbers in the number. 
Testcase: 
Input: 123456789 → Output: 3 
Input: 987531 → Output: 2'''

a = int(input("Enter a Number: "))
count = 0
while a > 0:
    digit = a % 10
    if digit == 1 or digit == 4 or digit == 9:
        count = count + 1
    a = a // 10
print("Output: ", count)

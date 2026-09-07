'''Question: Write a program to get a number from the user and print the total number of 
single-digit prime numbers in the number.
Testcase: 
Input: 163496481 → Output: 1 
Input: 364925 → Output: 3'''

a = int(input("Enter a Number: "))
count = 0
while a > 0:
    digit = a % 10
    if digit == 2 or digit == 3 or digit == 5 or digit == 7:
        count = count + 1
    a = a // 10
print("Output: ", count)

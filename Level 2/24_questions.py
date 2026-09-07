'''Question: Write a program to get a number from the user and print the total number of 
two-digit perfect square numbers in the number. 
Testcase: 
Input: 163496481 → Output: 4 
Input: 364925 → Output: 4'''

a = int(input("Enter a Number: "))
count = 0
while a >= 10:
    digit = a % 100
    if digit == 16 or digit == 25 or digit == 36 or digit == 49 or digit == 64 or digit == 81:
        count = count + 1
    a = a // 10
print("Output: ", count)

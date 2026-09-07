'''Question: Write a program to get a number from the user and print the total number of 
digits in that number. 
 
Testcase: 
Input: 123456 → Output: 6 
Input: 76895439 → Output: 8 
Input: 675 → Output: 3 '''

a = int(input("Enter a number: "))
count = 0
while a > 0:
    a = a // 10
    count = count + 1
print("Output: ", count)

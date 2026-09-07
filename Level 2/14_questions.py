'''Question: Write a program to get a number from the user and interchange the first and 
last digits, then print the result. 
Testcase: 
Input: 123456 → Output: 623451 
Input: 76895439 → Output: 96895437 
Input: 675 → Output: 576 '''

a = int(input("Enter a Number: "))
last = a % 10
temp = a
while temp >= 10:
    temp = temp // 10
first = temp
digits = 0
temp = a
while temp > 0:
    digits = digits + 1
    temp = temp // 10
middle = (a % (10 ** (digits - 1))) // 10
result = last * (10 ** (digits - 1)) + middle * 10 + first
print("Output: ", result)

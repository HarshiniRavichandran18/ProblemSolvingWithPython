'''Question: Write a program to print the total count of numbers less than 100000 whose 
sum of digits is 14. 
Testcase: 
Output: 4995'''

count = 0
for i in range(1, 100000):
    a = i
    sum = 0
    while a > 0:
        sum = sum + (a % 10)
        a = a // 10
    if sum == 14:
        count = count + 1
print("Output: ", count)

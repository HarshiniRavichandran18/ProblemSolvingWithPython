'''Question: Write a program to get a number from the user and print whether the last two 
digits form a prime number. 
Testcase: 
Input: 359 → Output: Prime 
Input: 3577 → Output: Not Prime '''

a = int(input("Enter a Number: "))
last = a % 100
count = 0
for i in range(1, last + 1):
    if last % i == 0:
        count = count + 1
if count == 2:
    print("Prime")
else:
    print("Not Prime")

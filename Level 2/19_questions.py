'''Question: Write a program to get a 4-digit number from the user and print whether the 
middle two digits form a prime number. 
Testcase: 
Input: 6359 → Output: Not Prime 
Input: 3517 → Output: Prime '''

a = int(input("Enter a 4-digit Number: "))
middle = (a // 10) % 100
count = 0
for i in range(1, middle + 1):
    if middle % i == 0:
        count = count + 1
if count == 2:
    print("Prime")
else:
    print("Not Prime") 

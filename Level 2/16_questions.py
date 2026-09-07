'''Question: Write a program to get a number from the user and print whether that number 
is prime or not. 
Testcase: 
Input: 31 → Output: Prime 
Input: 27 → Output: Not Prime'''

a = int(input("Enter a Number: "))
count = 0
for i in range(1, a + 1):
    if a % i == 0:
        count = count + 1
if count == 2:
    print("Prime")
else:
    print("Not Prime")
  

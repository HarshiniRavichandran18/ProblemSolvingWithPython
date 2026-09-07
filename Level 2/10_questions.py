'''Question: Write a loop program to print the sum of two-digit odd numbers whose ten's 
digit is 7. 
 
Testcase: 
Output: 375'''

sum = 0
for i in range(10, 100):
    if i % 2 != 0 and i // 10 == 7:
        sum = sum + i
print("Output: ", sum)

'''Question: Get a number from user and subtract 5 from that number and print the result. 
Write your code inside the function. 
Testcase: 
Input: 45 → Output: 40 
Input: 56789 → Output: 56784 '''

def check(a):
    return a - 5
a = int(input("Enter a Number: "))
print("Output: ", check(a))

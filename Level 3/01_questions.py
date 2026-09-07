'''Question: Get a number from user and add 2 to that number and print the result. Write 
your code inside the function. 
Testcase: 
Input: 45 → Output: 47 
Input: 56789 → Output: 56791'''

def check(a):
    return a + 2
a = int(input("Enter a Number: "))
print("Output: ", check(a))

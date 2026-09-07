'''Question: Get a number from user and check whether it is prime or not, then print the 
result. 
Testcase: 
Input: 61 → Output: Number is Prime 
Input: 1200 → Output: Number is not Prime'''

def check(a):
    count = 0
    for i in range(1, a + 1):
        if a % i == 0:
            count = count + 1
    if count == 2:
        return "Number is Prime"
    else:
        return "Number is not Prime"
a = int(input("Enter a Number: "))
print("Output: ", check(a))

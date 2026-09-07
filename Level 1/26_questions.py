'''Question: Get a two-digit number from user. If the sum of the digits is 10 then print "Success", 
otherwise print "Failure". 
Testcase: 
Input: 56 → Output: Failure 
Input: 37 → Output: Success'''

a = int(input("Enter a Number: "))
def check(a):
    if (a // 10) + (a % 10) == 10:
        return "Success"
    else:
        return "Failure"
print("Output: ", check(a))

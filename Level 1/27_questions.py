'''Question: Get a three-digit number from user. If the sum of the digits is 10 then print "Success", 
otherwise print "Failure". 
Testcase: 
Input: 956 → Output: Failure 
Input: 127 → Output: Success'''

a = int(input("Enter a Number: "))
def check(a):
    if (a // 100) + ((a // 10) % 10) + (a % 10) == 10:
        return "Success"
    else:
        return "Failure"
print("Output: ", check(a))

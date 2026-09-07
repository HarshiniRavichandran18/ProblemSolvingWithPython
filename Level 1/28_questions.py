'''Question: Get a three-digit number from user. If the sum of the one's digit and hundred's digit is 
less than 10, then print "Success", otherwise print "Failure". 
Testcase: 
Input: 569 → Output: Failure 
Input: 316 → Output: Success'''

a = int(input("Enter a Number: "))
def check(a):
    if (a % 10) + (a // 100) < 10:
        return "Success"
    else:
        return "Failure"
print("Output: ", check(a))

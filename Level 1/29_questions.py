'''Question: Get a four-digit number from user. If the sum of the ten's digit and hundred's digit is 
greater than 10, then print "Success", otherwise print "Failure". 
Testcase: 
Input: 7529 → Output: Failure 
Input: 9386 → Output: Success '''

a = int(input("Enter a Number: "))
def check(a):
    if (a % 10) + (a // 100) < 10:
        return "Success"
    else:
        return "Failure"
print("Output: ", check(a))

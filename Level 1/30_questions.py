'''Question: Get a four-digit number from user. If the sum of the ten's digit and hundred's digit is 
equal to 10, and one of the digits is more than 7 then print "Success", otherwise print "Failure". 
Testcase: 
Input: 4649 → Output: Failure 
Input: 9286 → Output: Success '''

a = int(input("Enter a Number: "))
def check(a):
    if (a // 10) % 10 + (a // 100) % 10 == 10 and ((a // 10) % 10 > 7 or (a // 100) % 10 > 7):
        return "Success"
    else:
        return "Failure"
print("Output: ", check(a))

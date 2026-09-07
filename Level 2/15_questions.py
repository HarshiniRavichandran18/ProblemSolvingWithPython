'''Question: Write a program to get a number from the user. If the first digit is even, print 
the same number. If the first digit is odd, subtract 1 from the first digit and print the 
number. 
Testcase: 
Input: 123456 → Output: 023456 
Input: 96895439 → Output: 86895439 
Input: 675 → Output: 675 
Input: 575 → Output: 475 '''

a = int(input("Enter a Number: "))
def check(a):
    first = a
    while first >= 10:
        first = first // 10
    if first % 2 == 0:
        return a
    else:
        return a - (10 ** (len(str(a)) - 1))
print("Output: ", check(a))

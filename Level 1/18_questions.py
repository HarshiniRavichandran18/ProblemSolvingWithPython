'''Question: Get a two-digit number from user and make the ten's digit 1, then print it. 
Testcase: 
Input: 95 → Output: 15 
Input: 82 → Output: 12 '''

a = int(input("Enter a number: "))
def tens(a):
    return 10 + (a % 10)
print("Output: ", tens(a))

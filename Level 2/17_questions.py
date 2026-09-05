a = int(input("Enter a Number: "))
count = 0
for i in range(1, a + 1):
    if a % i == 0:
        count = count + 1
sum = (a // 10) + (a % 10)
if count == 2:
    if sum == 14:
        print("Prime & Sum of Digits is 14")
    else:
        print("Prime, but sum of Digits is not 14")
else:
    if sum == 14:
        print("Not Prime but sum of digits is 14")
    else:
        print("Not Prime and sum of Digits is not 14")
      

a = int(input("Enter a 4-digit Number: "))
middle = (a // 10) % 100
count = 0
for i in range(1, middle + 1):
    if middle % i == 0:
        count = count + 1
if count == 2:
    print("Prime")
else:
    print("Not Prime")
  

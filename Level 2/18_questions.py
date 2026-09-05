a = int(input("Enter a Number: "))
last = a % 100
count = 0
for i in range(1, last + 1):
    if last % i == 0:
        count = count + 1
if count == 2:
    print("Prime")
else:
    print("Not Prime")
  

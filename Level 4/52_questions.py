a = input("Enter Main String: ")
b = input("Enter Substring: ")
position = a.find(b)
if position != -1:
    print("Output: ", position + 1)
else:
    print("Output: Not Found")
  

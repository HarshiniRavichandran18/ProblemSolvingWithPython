for i in range(99999999, 9999999, -1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count = count + 1
    if count == 2:
        print("Output: ", i)
        break
      

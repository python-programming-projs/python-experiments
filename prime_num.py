for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num/i
            print("%d equals %d * %d" % (num, i, j))
            break  # to move to the next number, the #first FOR
    else:  # else part of the loop
      print(str(num) + ' is a prime number')

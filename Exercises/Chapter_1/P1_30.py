def countDivideByTwo(num):
    if num < 2:
        print('Can not divide by two.')
    count = 0;
    while (num > 2):
        num = num / 2.0
        print(num)
        count += 1
    print('This number can be divided by two %d times before being less than two. Wow.' % (count))

countDivideByTwo(3)
countDivideByTwo(10)
countDivideByTwo(235)
countDivideByTwo(856)

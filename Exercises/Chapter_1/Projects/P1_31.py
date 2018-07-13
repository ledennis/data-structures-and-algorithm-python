def change(given, cost):
    billsDict = {100.00:'One Hundred', 50.00:'Fifty', 20.00:'Twenty', 10.00:'Ten', 5.00:'Five', 1.00:'One'}
    billsList = [100.00, 50.00, 20.00, 10.00, 5.00, 1.00]
    coinsDict = {0.25:'Quarter', 0.10:'Dime', 0.05:'Nickel', 0.01:'Penny'}
    coinsList = [0.25, 0.10, 0.05, 0.01]
    moneyList = billsList + coinsList
    moneyDict = billsDict.copy()
    moneyDict.update(coinsDict)
    response = 'I owe you, '
    delimSpace = ' '
    delimComma = ','
    delimPeriod = '.'
    totalResponse = 'totaling to '
    total = 0

    if (changeable(given, cost)):
        diff = given - cost
        total = diff

        for money in moneyList:
            if (diff / money >= 1):
                divMoney = diff // money
                diff = diff - (money * divMoney)
                response += str(divMoney) + delimSpace + moneyDict[money]
                if (diff != 0):
                    response += delimComma + delimSpace

        return response + totalResponse + str(total) + delimPeriod



def changeable(given, cost):
    if (cost > given):
        print('You owe me more money!')
        return False
    else:
        return True

print(change(100, 50))
print(change(123.45, 67.89))

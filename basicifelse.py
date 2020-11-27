money = 3000
expense = [100,200,2000]

money = money - sum(expense)
print(f'now I have {money} dollars')

if money >= 200:
    print('let\'s have Japanese food')
elif money >=100:
    print('let\'s have KFC')
else:
    print('let\'s have fast food')

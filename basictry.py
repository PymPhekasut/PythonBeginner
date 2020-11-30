

#money = int(input('Please enter the amount number: '))

#print (f'Your available balance: {money} AUD')

#print ('Your available balance: {:,d} AUD'.format(money))


#exceptions>check error

try:

    money = int(input('Enter the salary: '))
    print ('Your available salary: {:,d} AUD'.format(money))
except Exception as e:
    print('ERROR:',e)
else:
        print ('Extra paid x 10: {} AUD '.format(money*10))

print('Finish')



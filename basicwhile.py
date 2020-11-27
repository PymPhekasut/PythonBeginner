money = 100
print(f'available balance: {money} dollars')
transfer = int(input('How much do you want to withdraw: '))
print('check',money < transfer)

running = True

while money < transfer: #while loop until meet condition
    print('your account have less amount')
    print('-------------------------------------')
    print('press [1] deposit')
    print('press [2] insert the transaction amount')
    print('press [3] exit')
    
    menu = input('Please select the menu: ')
    if menu == '1': #if else condition
        get = int(input('deposit: '))
        money = money + get #money += get
    elif menu == '2':
        transfer = int(input('Please insert amount again: '))
    else:
        running = False #exit the program
        break
    
   
    print('-------------------------------------')

if running == True:
    print(f'result: transaction of {transfer} dollars is successful')
    money = money - transfer
    print(f'Your available balance: {money} dollars')
else:
    print('the transaction is cancelled')

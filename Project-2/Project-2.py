

total_balance=0
while True:
    print('\nWELOCOME TO OUR SERVICES \n')
    print(' THE SERVICES ARE \n 1- ADD BALANCE \n 2- DISPLAY BALANCE \n 3- WITHDRAW BALANCE \n 4- EXIT ')
    try:
      choice=int(input('enter the number of service you want   '))
    except ValueError:
        print('ENTER THE VALID NUMBER') 
        continue    
    if choice==1:
        try:
          amount=int(input('ENTER THE AMOUNT YOU WANNA ADD    '))
          total_balance+=amount
        except ValueError:
               print('PLEASE ENTER VALID AMOUNT')
    elif choice==2:
        print(f'YOUR CURRENT BALANCE IS  {total_balance} ') 
    elif choice==3:
        try:
            wamount=int(input('ENTER THE AMOUNT YOU WANNA WITHDRAW     '))
            if wamount<=total_balance:
             total_balance-=wamount
             print(f'{wamount} IS WITHDRAWN FROM YOUR BALANCE')
            else:
                print('PLEASE ENTER THE VALID AMOUNT')
        except ValueError:
            print('PLEASE ENTER VALID AMOUNT')
    elif choice==4:
        print('EXITING PROGRAM...')
        break
    else :
        print('PLEASE ENTER THE NUMBER FROM GIVEN OPTIONS 1,2,3')

#Project 1 - Currency Converter without live data - AED,EUR,INR,USD (Short Version) - User enters amount and currency that he wants to convert and chooses two other currencies that he wants to convert to. (3 currency amounts - 1 currency amount that user wants to convert and 2 currency amounts that user wants to convert to)
n=1
while n==1:
    print('\nWelcome to Currency Converter.\n')
    print('Press Enter to continue')
    input() #interactive input
    x=1 #initialized variables x and y for starting while loop
    y=1
    z=1
    data=1
    while data==1:
        try: #if code inside this runs, then except block code won't run and if the code inside this fails, then code inside except block runs.
            amount_user=input('Enter amount to convert : ') #user amount input stored in amount_user. Now there are chances of someone entering a random thing - not particularly a number or something. He can enter say 'Wassup'. In that case, it will throw an error in the next line as it won't be converted to float. To avoid that, we use try and except structure around this section of code.
            amount_user=float(amount_user) #string to float
            data=0
        except:
            print('Bad data entered as amount. Please enter a suitable amount')
            data=1
    print('Choose currency that you would like to convert\n')
    while x==1:
        currency_user=input('Make an appropriate choice: \n1. AED \n2. EUR \n3. INR \n4. USD \n') #currency choice that you want to convert
        if currency_user=='1':
            factor=[1,0.24,18.83,0.27] #factor variable stores an array of possibility of values used as multiplication factor if currency_user is 1
            break #break out of loop like x=0
        elif currency_user=='2':
            factor=[4.12,1,77.56,1.12]
            break
        elif currency_user=='3':
            factor=[0.053,0.013,1,0.014]
            break
        elif currency_user=='4':
            factor=[3.67,0.89,69.18,1]
            break
        else:
            print('OOPS.You made a wrong choice.Please choose currency that you would like to convert again\n') #repeat step 11 hence while loop but loop repeated only if  you enter else block
            continue #continue loop like x=1
    print('\nChoose first currency that you would like to convert to\n')
    while y==1:
        currency_convert=input('Make an appropriate choice: \n1. AED \n2. EUR \n3. INR \n4. USD \n') #currency choice that you want to convert to
        if int(currency_convert)==1 or int(currency_convert)==2 or int(currency_convert)==3 or int(currency_convert)==4:
                    y=0
        else:
            print('OOPS.You made a wrong choice.Please choose first currency that you would like to convert to again\n') #if incorrect input then repeat step 29 hence while loop but loop repeated only if you enter else block
            y=1
    print('\nChoose second currency that you would like to convert to\n')
    while z==1:
        currency_convert2=input('Make an appropriate choice: \n1. AED \n2. EUR \n3. INR \n4. USD \n') #currency choice that you want to convert to
        if int(currency_convert2)==1 or int(currency_convert2)==2 or int(currency_convert2)==3 or int(currency_convert2)==4:
                    z=0
        else:
            print('OOPS.You made a wrong choice.Please choose second currency that you would like to convert to again\n') #if incorrect input then repeat step 29 hence while loop but loop repeated only if you enter else block
            z=1

    amount_convert=amount_user*factor[int(currency_convert)-1] #amount_convert stores value after conversion
    amount_convert2=amount_user*factor[int(currency_convert2)-1]
    print('\nAmount after first conversion :',amount_convert)
    print('\nAmount after second conversion :',amount_convert2)

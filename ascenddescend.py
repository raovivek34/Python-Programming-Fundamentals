#Project 2 - From a list of numbers, retrieve the numbers and sort them in descending order or ascending order depending on the choice you make.
#eg. [1,2,3,4,5] >> List of numbers - Retrieve numbers and sort them in descending order. eg. 5 4 3 2 1 or in ascending order. eg. 1 2 3 4 5
lst=[] #Initially we will ask the user to make list of numbers themselves
while True:
    try:
        a=input('\nEnter how many numbers do you want in the list : ')
        a=int(a)
        break
    except:
        print('\nBad data entered. Try again.')
        continue
for i in range(0,a): #Definite Loop - indicating no. of iterations = no. of numbers you want to append in the list
    while True:
        try:
            x=input('\nStart entering numbers in the list one by one : \n')
            x=float(x)
            break
        except:
            print('Bad data entered. Try again.')
            continue
    lst.append(x) #Append number to the list
print('\nYour list of numbers is :',lst) #This is the list of numbers you made
while True:
    print('\nMake a choice : \n')
    choice=input('1. Sort numbers in descending order\n2. Sort numbers in ascending order\n')
    if choice=='1':
        print('\nRetrieving numbers from the list and sorting them in descending order : \n')
        while len(lst)!=0: #Will retrieve numbers in descending order and print them until the list is empty.
            print(max(lst))
            lst.remove(max(lst)) #Remove maximum element from the list
        break
    elif choice=='2':
        print('\nRetrieving numbers from the list and sorting them in ascending order : \n')
        while len(lst)!=0: #Will retrieve numbers in ascending order and print them until the list is empty.
            print(min(lst))
            lst.remove(min(lst)) #Remove minimum element from the list
        break
    else:
        print('Bad data entered. Try again')
        continue
print('\nDone')
